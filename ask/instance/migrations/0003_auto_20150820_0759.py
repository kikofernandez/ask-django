# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0002_auto_20150820_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cancellable',
            field=models.BooleanField(default=False, help_text=b"Should it be cancelled if it doesn't reach minimum number of people?"),
        ),
        migrations.AddField(
            model_name='service',
            name='no_people',
            field=models.IntegerField(default=1, help_text=b'Number of people for the service'),
        ),
        migrations.AddField(
            model_name='service',
            name='priority',
            field=models.IntegerField(default=200, choices=[(300, b'High'), (200, b'Normal'), (100, b'Low')]),
        ),
        migrations.AddField(
            model_name='service',
            name='state',
            field=models.CharField(default=b'IP', max_length=2, choices=[(b'FU', b'Fulfilled'), (b'CA', b'Cancelled'), (b'IP', b'In Progress'), (b'PP', b'Pending Payment')]),
        ),
        migrations.RemoveField(
            model_name='service',
            name='assigned',
        ),
        migrations.AddField(
            model_name='service',
            name='assigned',
            field=models.ManyToManyField(related_query_name=b'services', related_name='service', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='skills',
            field=models.ManyToManyField(help_text=b'Select the required skills', related_name='skill', related_query_name=b'skills', to='instance.Skill'),
        ),
        migrations.AlterField(
            model_name='service',
            name='user_request',
            field=models.ForeignKey(related_query_name=b'authors', related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
