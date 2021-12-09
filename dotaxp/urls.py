from django.urls import path

from . import views

app_name = 'dotaxp'

urlpatterns = [
    path(
        'hero-stat-progression/',
        views.get_hero_stat_progression,
        name='hero-stat-progression',
    ),
]
