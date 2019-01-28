# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-27 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion_telefonia_app', '0003_attr_hangup_dest_entrante'),
        ('ominicontacto_app', '0005_agenteencontacto_es_originario'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='destino',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='campanas_destino_failover',
                to='configuracion_telefonia_app.DestinoEntrante'),
        ),
    ]
