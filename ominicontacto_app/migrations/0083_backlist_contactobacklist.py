# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-16 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ominicontacto_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0082_grupo_auto_unpause'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('archivo_importacion', models.FileField(max_length=256, upload_to=ominicontacto_app.models.upload_to)),
                ('nombre_archivo_importacion', models.CharField(max_length=256)),
                ('sin_definir', models.BooleanField(default=True)),
                ('cantidad_contactos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContactoBacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=128)),
                ('back_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contactosbacklist', to='ominicontacto_app.Backlist')),
            ],
        ),
    ]