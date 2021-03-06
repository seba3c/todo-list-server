# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('foreground_color', models.CharField(default='000000', max_length=20, verbose_name='Foreground Color')),
                ('background_color', models.CharField(default='ffffff', max_length=20, verbose_name='Foreground Color')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Labels',
                'verbose_name': 'Label',
            },
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created_at'], 'verbose_name': 'TODO-LIST', 'verbose_name_plural': 'TODO-LISTs'},
        ),
        migrations.AddField(
            model_name='todolist',
            name='labels',
            field=models.ManyToManyField(to='todolist.Label'),
        ),
    ]
