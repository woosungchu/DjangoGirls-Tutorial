# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20160521_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('post_type', models.CharField(max_length=50, default='All')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='symbol',
            name='symbols',
        ),
        migrations.AlterField(
            model_name='symbol',
            name='font',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='symbol',
            name='category',
            field=models.ForeignKey(to='blog.Category', null=True),
        ),
    ]
