# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todolist_text',
            new_name='To_Do',
        ),
        migrations.AddField(
            model_name='todolist',
            name='Title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
