# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('sitesettings', '0001_initial'), ('sitesettings', '0002_auto_20171104_1223')]

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtm_id', models.CharField(blank=True, max_length=50)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
