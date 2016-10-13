# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_socialmediareference_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediareference',
            name='author',
            field=models.ForeignKey(related_name='social_medias', to='articles.Author'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ForeignKey(related_name='tags', to='articles.Article'),
        ),
    ]
