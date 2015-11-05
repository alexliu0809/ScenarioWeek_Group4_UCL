# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0004_todolist_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todolist_text',
            new_name='To_Do',
        ),
    ]
