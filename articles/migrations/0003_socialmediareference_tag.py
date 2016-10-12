# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_outlet'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaReference',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('social_media', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('author', models.ForeignKey(to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
        ),
    ]
