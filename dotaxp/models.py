from django.db import models
from django.core.validators import MaxValueValidator


class Hero(models.Model):
    class Meta:
        verbose_name_plural = 'heroes'

    class Attribute:
        AGILITY = 'AGI'
        INTELLIGENCE = 'INT'
        STRENGTH = 'STR'
        CHOICES = [
            (AGILITY, 'Agility'),
            (INTELLIGENCE, 'Intelligence'),
            (STRENGTH, 'Strength'),
        ]

    name = models.CharField(max_length=30)
    main_attr = models.CharField(
        max_length=3,
        choices=Attribute.CHOICES,
    )

    init_agi = models.IntegerField(default=0)
    init_int = models.IntegerField(default=0)
    init_str = models.IntegerField(default=0)

    gain_agi = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    gain_int = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    gain_str = models.DecimalField(decimal_places=1, max_digits=4, default=0)

    def __str__(self):
        return f'{self.name} ({self.main_attr})'


class HeroLife(models.Model):
    class Meta:
        verbose_name_plural = 'hero lives'

    hero = models.ForeignKey('Hero', on_delete=models.CASCADE)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(30)])

    @property
    def current_agi(self):
        return self.hero.init_agi + self.hero.gain_agi * self.level

    @property
    def current_int(self):
        return self.hero.init_int + self.hero.gain_int * self.level

    @property
    def current_str(self):
        return self.hero.init_str + self.hero.gain_str * self.level
