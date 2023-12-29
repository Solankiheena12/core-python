from rest_framework_nested import routers

# user:
from user.views import UserViewSet

# zone:
from zone.views import ZoneViewSet, ZoneNameDeleteViewSet, ZoneNameArchiveViewSet

# pincode:
from pincode.views import PincodeViewSet, PincodeDeleteViewSet, PincodeArchiveViewSet


router = routers.DefaultRouter()

# user:
router.register("user", UserViewSet, basename="user")

# zone:
router.register("zone", ZoneViewSet, basename="zone")
router.register("zone-delete", ZoneNameDeleteViewSet, basename="zone_delete")
router.register("zone-archive", ZoneNameArchiveViewSet, basename="zone_archive")

# pincode:
router.register("pincode", PincodeViewSet, basename="pincode")
router.register("pincode-delete", PincodeDeleteViewSet, basename="pincode_delete")
router.register("pincode-archive", PincodeArchiveViewSet, basename="pincode_archive")


# admin :
# email: darshan@gmail.com
# password: darshan1210
