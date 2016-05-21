# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_symbol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symbol',
            name='colors',
        ),
        migrations.AddField(
            model_name='symbol',
            name='main_color',
            field=colorfield.fields.ColorField(max_length=10, default='#e6ccff'),
        ),
        migrations.AddField(
            model_name='symbol',
            name='sub_color',
            field=colorfield.fields.ColorField(max_length=10, default='#ccff99'),
        ),
    ]
