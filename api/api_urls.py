from rest_framework.routers import DefaultRouter

from cake.api_views import CakeCreateListViewSet

app_name = 'api'

router = DefaultRouter()
router.register('cake', CakeCreateListViewSet, basename='cake')

urlpatterns = router.urls
