# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_reviewer_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Book',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='User',
            new_name='user',
        ),
    ]
