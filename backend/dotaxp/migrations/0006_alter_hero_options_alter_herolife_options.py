# Generated by Django 4.0 on 2021-12-08 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotaxp', '0005_alter_hero_options_alter_herolife_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name_plural': 'heroes'},
        ),
        migrations.AlterModelOptions(
            name='herolife',
            options={'verbose_name_plural': 'hero lives'},
        ),
    ]