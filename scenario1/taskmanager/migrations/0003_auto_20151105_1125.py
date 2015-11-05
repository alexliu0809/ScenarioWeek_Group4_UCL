# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20151104_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='To_Do',
            new_name='todolist_text',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='Title',
        ),
    ]
