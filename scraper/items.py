# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from articles.models import Article, Author, Outlet
from scrapy_djangoitem import DjangoItem


class ArticleItem(DjangoItem):
    django_model = Article


class AuthorItem(DjangoItem):
    django_model = Author


class OutletItem(DjangoItem):
    django_model = Outlet