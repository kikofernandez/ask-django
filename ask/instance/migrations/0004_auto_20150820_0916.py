# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0003_auto_20150820_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(blank=True, null=True, choices=[(500, b'Excellent'), (400, b'Very good'), (300, b'Good'), (200, b'Poor'), (100, b'Disaster')])),
                ('performer', models.ForeignKey(related_name='performer_rating', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(related_name='request_rating', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(to='instance.Service')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('service', 'performer', 'requester')]),
        ),
    ]
