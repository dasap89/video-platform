# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('rent_start_time', models.DateTimeField(null=True, auto_now=True)),
                ('rent_by', models.CharField(max_length=200, null=True)),
                ('rent_by_phone', models.CharField(max_length=20, blank=True, null=True)),
                ('rent_available', models.BooleanField(default=True)),
                ('rent_manager', models.ForeignKey(related_name='rent_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
