# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encuesta', models.CharField(max_length=256, verbose_name=b'ID Encuesta')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Individuo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('individuo', models.CharField(max_length=256, verbose_name=b'ID Individuo')),
                ('nombres', models.CharField(max_length=256)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=256, choices=[(b'Masculino', b'masculino'), (b'Femenino', b'femenino'), (b'Otro', b'otro')])),
                ('tiempo_residencia', models.IntegerField(default=0)),
                ('problema_salud', models.BooleanField(verbose_name=b'Problemas de salud en los ultimos 20 a\xc3\xb1os')),
            ],
        ),
        migrations.CreateModel(
            name='Pueblo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=256)),
                ('numero', models.IntegerField()),
                ('manzana', models.CharField(max_length=256)),
                ('lote', models.IntegerField()),
                ('agua', models.BooleanField(verbose_name=b'Tiene agua de red?', choices=[(b'Agua de red', b'red'), (b'Agua de Pozo', b'pozo'), (b'Otra fuente de agua', b'otra')])),
                ('pavimento', models.BooleanField(verbose_name=b'Calle Pavimentada')),
                ('num_fallecidos', models.IntegerField(default=0)),
                ('pueblo', models.ForeignKey(to='encuestas.Pueblo')),
            ],
        ),
        migrations.AddField(
            model_name='individuo',
            name='vivienda',
            field=models.ForeignKey(to='encuestas.Vivienda'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='vivienda',
            field=models.OneToOneField(to='encuestas.Vivienda'),
        ),
    ]
