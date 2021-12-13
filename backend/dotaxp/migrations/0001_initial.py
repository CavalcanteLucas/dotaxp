# Generated by Django 4.0 on 2021-12-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=30)),
                ('strength', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('agility', models.IntegerField()),
                (
                    'main_attribute',
                    models.CharField(
                        choices=[
                            ('STR', 'Strength'),
                            ('AGI', 'Agility'),
                            ('INT', 'Intelligence'),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
    ]