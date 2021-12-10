from django.urls import path
from rest_framework import routers

from dotaxp.models import Hero

from .views import (
    get_hero_stat_progression,
    HeroViewSet,
)

app_name = 'dotaxp'

router = routers.DefaultRouter()
router.register('heroes', HeroViewSet, basename='heroes')

urlpatterns = [
    path(
        'hero-stat-progression/',
        get_hero_stat_progression,
        name='hero-stat-progression',
    ),
]

urlpatterns += router.urls
