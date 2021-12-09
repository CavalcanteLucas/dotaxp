import json

from django.http import HttpResponse

from .models import Hero

def get_hero_stat_progression(request):
    context = dict()
    abaddon = Hero.objects.get(name="Abaddon")
    alchemist = Hero.objects.get(name="Alchemist")

    context['progression'] = {
        'abaddon': abaddon.get_stats_progression(),
        'alchemist': alchemist.get_stats_progression(),
    }
    return HttpResponse(json.dumps(context), content_type='application/json')
