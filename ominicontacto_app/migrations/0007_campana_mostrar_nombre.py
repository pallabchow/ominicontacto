# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-29 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0006_queue_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='campana',
            name='mostrar_nombre',
            field=models.BooleanField(default=True),
        ),
    ]
