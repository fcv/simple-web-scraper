from django.http import HttpResponse, Http404, HttpResponseBadRequest
from simple_web_scraper import models
from .models import Author, AuthorSerializer, Article, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleList(APIView):
    """
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        articles = models.articles
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):

    def get_object(self, id):
        try:
            id = int(id)
        except ValueError:
            raise HttpResponseBadRequest()
        article = next(filter(lambda a: a.id == id, models.articles), None)
        if article is None:
            raise Http404
        return article

    def get(self, request, id, format=None):
        article = self.get_object(id)
        serializer = AuthorSerializer(article)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        article = self.get_object(id)
        # article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorList(APIView):
    """
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/authors

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        authors = models.authors
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_object(self, id):
        try:
            id = int(id)
        except ValueError:
            raise HttpResponseBadRequest()
        author = next(filter(lambda a: a.id == id, models.authors), None)
        if author is None:
            raise Http404
        return author

    def get(self, request, id, format=None):
        author = self.get_object(id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        author = self.get_object(id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        author = self.get_object(id)
        # author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
