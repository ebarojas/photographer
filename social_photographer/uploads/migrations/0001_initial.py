# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('price', models.BigIntegerField()),
                ('tuit', models.CharField(max_length=200)),
                ('shot', models.ImageField(upload_to=b'showcase_pics')),
                ('created_at', models.DateField()),
            ],
        ),
    ]
