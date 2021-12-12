from django.urls import path
from rest_framework import routers

from dotaxp.models import Hero

from .views import (
    HeroViewSet,
)

app_name = 'dotaxp'

router = routers.DefaultRouter()
router.register('heroes', HeroViewSet, basename='heroes')


urlpatterns = router.urls
