# Generated by Django 2.1.2 on 2018-10-16 01:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('playtime', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(upload_to='')),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('players', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
