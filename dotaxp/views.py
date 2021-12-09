import json

from django.http import HttpResponse

from .models import Hero

def get_hero_stat_progression(request):
    context = dict()
    abaddon = Hero.objects.get(name="Abaddon")
    context['progression'] = abaddon.get_str_progression()
    return HttpResponse(json.dumps(context), content_type='application/json')
