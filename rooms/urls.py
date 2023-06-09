from rest_framework.routers import SimpleRouter
from .views import RoomViewSet

router = SimpleRouter()

router.register('rooms', RoomViewSet)

urlpatterns = []