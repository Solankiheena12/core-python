from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.pagination import Pagination

from category_tree.models import CategoryTree
from category_tree.serializers import CategoryTreeSerializer, CategoryTreeStatusSerializer

# Create your views here.


class CategoryTreeViewSet(ModelViewSet):
    queryset = CategoryTree.objects.filter(deleted=0).order_by("id")
    serializer_class = CategoryTreeSerializer
    pagination_class = Pagination
    filter_backends = [SearchFilter, OrderingFilter]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    search_fields = ["id", "category_name", "description", "status"]

    ordering_fields = ["id", "category_name", "description", "status"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response({"success": True, "data": serializer.data})

    def create(self, request, *args, **kwargs):
        data = request.data
        data["created_by"] = request.user.id
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": True, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = 1
        instance.save()
        return Response({"success": True, "message": "Category Destroyed Successfully"})




# Category Tree Status Change :

class CategoryTreeStatusViewset(ModelViewSet):
    queryset = CategoryTree.objects.filter(deleted=0).order_by("id")
    serializer_class = CategoryTreeStatusSerializer
    pagination_class = Pagination
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            categorytree = serializer.save()
            if categorytree.status == "Active":
                return Response({"success": True, "message": "Category Is Now Activated"}, status=status.HTTP_200_OK)

            else:
                return Response({"success": True, "message": "Category Has Been Deactived"}, status=status.HTTP_200_OK)

        else:
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# Category Tree Multiple Delete :
        
class CategoryTreeDeleteViewSet(ModelViewSet):
    queryset = CategoryTree.objects.filter(deleted=0).order_by('id')
    serializer_class = CategoryTreeSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = CategoryTreeDeleteViewSet(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Multiple Catergory archive Succefully"},
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )