from .views import TestView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/get', TestView)
urlpatterns = router.urls
