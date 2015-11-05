# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_auto_20151105_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Task', models.CharField(max_length=600)),
            ],
        ),
        migrations.AlterField(
            model_name='todolist',
            name='Title',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='tasks',
            name='Todolist',
            field=models.ForeignKey(to='taskmanager.Todolist'),
        ),
    ]
