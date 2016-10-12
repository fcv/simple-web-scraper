# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scraper.items import ArticleItem, AuthorItem, OutletItem


class DbStorePipeline(object):
    """
    Scrapy Pipeline that process DjangoItem instances calling `save` method on them
    in order to store its data in Database
    """

    def process_item(self, item, spider):

        # I suppose we could only check on DjangoItem
        if (isinstance(item, ArticleItem) or isinstance(item, AuthorItem) or isinstance(item, OutletItem)):
            item.save()

        return item
