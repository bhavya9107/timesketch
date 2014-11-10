# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sketch', '0009_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='timelines',
        ),
        migrations.AddField(
            model_name='sketchtimeline',
            name='sketch',
            field=models.ForeignKey(default=2, to='sketch.Sketch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sketchtimeline',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]