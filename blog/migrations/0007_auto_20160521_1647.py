# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160521_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symbol',
            name='font',
        ),
        migrations.AlterField(
            model_name='category',
            name='post_type',
            field=models.CharField(max_length=50),
        ),
    ]
