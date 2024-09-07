from django.urls import path, include
from rest_framework import routers

from .views import (
    EmbroideryViewSet,
    BookViewSet,
)

router = routers.DefaultRouter()
router.register("embroideries", EmbroideryViewSet)
router.register("books", BookViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "shop"
