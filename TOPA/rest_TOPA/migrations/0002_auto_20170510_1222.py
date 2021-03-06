# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_TOPA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='id',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='id',
        ),
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='rest_TOPA.Airline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='roundTrip',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='airline',
            name='code',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flightCode',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
