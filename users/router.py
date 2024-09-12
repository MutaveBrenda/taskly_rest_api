from rest_framework import routers

from .viewsets import UserViewset

app_name = "users"

router = routers.DefaultRouter()
router.register('users',UserViewset)