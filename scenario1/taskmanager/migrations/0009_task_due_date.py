# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0008_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Due_Date',
            field=models.CharField(default=0, max_length=600),
            preserve_default=False,
        ),
    ]
