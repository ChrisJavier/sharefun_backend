from app.viewsets import CustomerListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('app',  CustomerListViewSet, base_name='custom')
