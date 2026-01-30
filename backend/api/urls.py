from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, upload_csv

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', upload_csv),
]
