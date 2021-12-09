import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Hero
from .serializers import HeroSerializer

def get_hero_stat_progression(request):
    context = dict()
    abaddon = Hero.objects.get(name="Abaddon")
    alchemist = Hero.objects.get(name="Alchemist")

    context['progression'] = {
        'abaddon': abaddon.get_stats_progression(),
        'alchemist': alchemist.get_stats_progression(),
    }
    return HttpResponse(json.dumps(context), content_type='application/json')


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    @action(detail=True, methods=['get'])
    def get_stat_progression(self, request, pk=None):
        hero = Hero.objects.get(id=pk)
        context = dict()
        context['progression'] = {
            hero.name: hero.get_stats_progression()
        }
        return HttpResponse(json.dumps(context), content_type='application/json')
