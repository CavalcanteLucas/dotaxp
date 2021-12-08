from django.contrib import admin
from .models import Hero, HeroLife


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass


@admin.register(HeroLife)
class HeroLifeAdmin(admin.ModelAdmin):
    pass
