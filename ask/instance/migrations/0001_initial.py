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
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request', models.TextField()),
                ('assigned', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='skills',
            field=models.ManyToManyField(to='instance.Skill'),
        ),
        migrations.AddField(
            model_name='service',
            name='user_request',
            field=models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
