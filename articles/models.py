from django.db import models
from rest_framework import serializers


class Author(models.Model):

    name = models.CharField(max_length=100)
    profile_url = models.URLField()

    def __str__(self):
        return u'%s %s' % (self.id, self.name)


class SocialMediaReference(models.Model):

    social_media = models.CharField(max_length = 100)
    url = models.URLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "social_medias")

    def __str__(self):
        return u'%s %s %s' % (self.id, self.social_media, self.url)


class SocialMediaReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaReference
        fields = ('social_media', 'url')


class AuthorSerializer(serializers.ModelSerializer):

    social_medias = SocialMediaReferenceSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'profile_url', 'social_medias')


class Article(models.Model):

    title = models.CharField(max_length=100)
    url = models.URLField()
    authors = models.ManyToManyField(Author)
    publish_date = models.DateTimeField(blank=True,null=True)
    content = models.CharField(max_length=500)

    def __str__(self):
        return u'%s %s' % (self.id, self.title)


class Tag(models.Model):

    name = models.CharField(max_length=100)
    article = models.ForeignKey(Article, related_name = "tags")

    def __str__(self):
        return self.name


class ArticleSerializer(serializers.ModelSerializer):

    # set it readonly by now, consider implementing `StringRelatedField.to_internal_value()`
    # see example of error message:
    #     "StringRelatedField.to_internal_value()"
    tags = serializers.StringRelatedField(many=True, read_only=True)

    # set readonly by now, consider implementing `.create` method
    # see example of error message:
    #     "The `.create()` method does not support writable nested fields by default.
    #     Write an explicit `.create()` method for serializer `articles.models.ArticleSerializer`, or set `read_only=True` on nested serializer fields."
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'publish_date', 'content', 'authors', 'tags')


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