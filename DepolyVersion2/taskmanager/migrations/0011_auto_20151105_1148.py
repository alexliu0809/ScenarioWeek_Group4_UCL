# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0010_auto_20151105_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Due_Date',
            field=models.DateField(verbose_name=b'date due'),
        ),
    ]
