from rest_framework_nested import routers


from user.views import UserViewSet
from zone.views import ZoneViewSet
from pincode.views import PincodeViewSet


router = routers.DefaultRouter()

router.register("user", UserViewSet, basename="user")
router.register("zone", ZoneViewSet, basename="zone")
router.register("pincode", PincodeViewSet, basename="pincode")


# admin :
# email: darshan@gmail.com
# password: darshan1210
