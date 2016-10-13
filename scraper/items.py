# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from articles.models import Article, Author, Outlet
from scrapy_djangoitem import DjangoItem
from scrapy import Field


class ArticleItem(DjangoItem):
    django_model = Article
    tags = Field()
    author_profile_ids = Field()


class AuthorItem(DjangoItem):
    django_model = Author
    profile_image_url = Field()
    social_medias = Field()


class OutletItem(DjangoItem):
    django_model = Outlet