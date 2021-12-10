from django.db import models


class Hero(models.Model):
    class Meta:
        verbose_name_plural = 'heroes'

    class Attribute:
        AGI = 'AGI'
        INT = 'INT'
        STR = 'STR'
        CHOICES = [
            (AGI, 'Agility'),
            (INT, 'Intelligence'),
            (STR, 'Strength'),
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

    def get_agi_progression(self):
        return [
            float(self.init_agi + self.gain_agi * level)
            for level in range(1, 31)
        ]

    def get_int_progression(self):
        return [
            float(self.init_int + self.gain_int * level)
            for level in range(1, 31)
        ]

    def get_str_progression(self):
        return [
            float(self.init_str + self.gain_str * level)
            for level in range(1, 31)
        ]

    def get_stats_progression(self):
        return {
            self.Attribute.AGI: self.get_agi_progression(),
            self.Attribute.INT: self.get_int_progression(),
            self.Attribute.STR: self.get_str_progression(),
        }
