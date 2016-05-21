# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160521_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.RemoveField(
            model_name='symbol',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
