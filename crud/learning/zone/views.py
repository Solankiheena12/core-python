from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from utils.pagination import Pagination

from zone.models import Zone
from zone.serializers import ZoneSerializer, ZoneNameDeleteSerializer, ZoneNameArchiveSerializer

# Create your views here.


class ZoneViewSet(ModelViewSet):
    queryset = Zone.objects.filter(deleted=0).order_by("-id")
    serializer_class = ZoneSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = Pagination
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    search_fields = [
        "zone_name",
    ]

    ordering_fields = [
        "zone_name",
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response({"success": True, "data": serializer.data})

        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response({"success": True, "data": serializer.data})

    def create(self, request, *args, **kwargs):
        data = request.data
        data["created_by"] = request.user.id
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)

        else:
            error_messages = " ".join([", ".join(value) for value in serializer.errors.values()])
            print([", ".join(value) for value in serializer.errors.values()])
            # for value in serializer.errors.values():
            #     print(value)
                
            return Response({"success": False, "message": error_messages}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        data["updated_by"] = request.user.id
        serializer = self.serializer_class(instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"success": True, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = 1
        instance.save()
        return Response({"success": True, "message": "Zone Destroyed Successfully"}, status=status.HTTP_200_OK)
