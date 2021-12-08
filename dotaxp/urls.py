from django.urls import path

from . import views

app_name = 'dotaxp'

urlpatterns = [
    path('', views.index, name='index'),
]
