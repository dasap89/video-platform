# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='rent_by',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='rent_manager',
            field=models.ForeignKey(blank=True, null=True, related_name='rent_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
