import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Hero
from .serializers import HeroSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    @action(detail=True, methods=['get'])
    def get_stat_progression(self, request, pk=None):
        hero = Hero.objects.get(id=pk)
        context = dict()
        context['stats_progression'] = hero.get_stats_progression()
        return HttpResponse(
            json.dumps(context), content_type='application/json'
        )
