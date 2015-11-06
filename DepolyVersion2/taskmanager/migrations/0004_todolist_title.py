# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20151105_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='Title',
            field=models.CharField(default=0, max_length=600),
            preserve_default=False,
        ),
    ]
