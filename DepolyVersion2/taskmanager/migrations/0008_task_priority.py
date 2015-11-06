# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0007_auto_20151105_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Priority',
            field=models.IntegerField(default=0),
        ),
    ]
