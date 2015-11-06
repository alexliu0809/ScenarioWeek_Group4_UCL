# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0009_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Due_Date',
            field=models.DateTimeField(verbose_name=b'date due'),
        ),
    ]
