from django.db import models
from rest_framework import serializers

class Author(models.Model):

    name = models.CharField(max_length=100)
    profile_url = models.URLField()

    def __str__(self):
        return u'%s %s' % (self.id, self.name)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'profile_url')


class Article(models.Model):

    title = models.CharField(max_length=100)
    url = models.URLField()
    authors = models.ManyToManyField(Author)
    publish_date = models.DateTimeField(blank=True,null=True)
    content = models.CharField(max_length=500)

    def __str__(self):
        return u'%s %s' % (self.id, self.title)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'publish_date', 'content')


class Outlet(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField()
    logo_url = models.URLField()

    def __str__(self):
        return u'%s' % (self.name)


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ('id', 'name', 'description', 'url', 'logo_url')