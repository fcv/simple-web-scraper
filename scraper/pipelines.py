# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scraper.items import ArticleItem, AuthorItem, OutletItem
from articles.models import Article, Author, Outlet, Tag


class DbStorePipeline(object):
    """
    Scrapy Pipeline that process DjangoItem instances calling `save` method on them
    in order to store its data in Database
    """

    def process_item(self, item, spider):

        if isinstance(item, ArticleItem):
            return self.process_article(item)

        if isinstance(item, AuthorItem):
            return self.process_author(item)

        if isinstance(item, OutletItem):
            return self.process_outlet(item)

        return item

    def process_article(self, article_item):

        candidate_url = article_item['url']
        # if there already is a record with such URL then ignore it
        # TODO: Would it be better to update it ?
        if Article.objects.filter(url=candidate_url).count() > 0:
            return article_item

        # list of strings, like "jonathan-shieber" out of "/author/jonathan-shieber/"
        author_profile_ids = article_item['author_profile_ids']
        # list of strings
        tags = article_item['tags']

        article = article_item.save()

        for author_profile_id in author_profile_ids:
            for author in Author.objects.filter(profile_url__contains=author_profile_id):
                article.authors.add(author)

        for tag in tags:
            article.tags.create(name = tag)

        article.save()
        return article_item

    def process_author(self, author_item):

        candidate_url = author_item['profile_url']
        # if there already is a record with such profile URL then ignore it
        if Author.objects.filter(profile_url=candidate_url).count() > 0:
            return author_item

        author = author_item.save()

        # dictionary name ~> url
        social_medias = author_item['social_medias']
        for name, url in social_medias.items():
            author.social_medias.create(social_media = name, url = url)

        return author_item

    def process_outlet(self, outlet_item):

        candidate_url = outlet_item['url']
        if Outlet.objects.filter(url=candidate_url).count() > 0:
            return outlet_item

        outlet_item.save()
        return outlet_item