# Generated by Django 2.2.7 on 2020-05-05 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion_telefonia_app', '0011_playlist_musica_de_espera'),
        ('ominicontacto_app', '0048_campana_campos_de_restriccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='campana',
            name='outcid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campana',
            name='outr',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='configuracion_telefonia_app.RutaSaliente'),
        ),
    ]
