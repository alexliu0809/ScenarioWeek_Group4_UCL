# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0006_auto_20151105_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Task_text', models.CharField(max_length=600)),
            ],
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='Todolist',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='To_Do',
            new_name='Description',
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='Todolist',
            field=models.ForeignKey(to='taskmanager.Todolist'),
        ),
    ]
