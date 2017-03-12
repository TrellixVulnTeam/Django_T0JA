from .api import ListViewSets, CardViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSets)
router.register(r'cards', CardViewSets)

urlpatterns = router.urls