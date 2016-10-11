from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.db.models import Q
from articles.models import Author, AuthorSerializer, Article, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


class ArticleList(APIView):
    """
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        articles = Article.objects.all()
        if 'q' in request.GET:
            q = request.GET['q']
            if q:
                query = Q(title__icontains = q) | Q(content__icontains = q)
                articles = articles.filter(query)

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):

    def get_object(self, id):
        try:
            id = int(id)
        except ValueError:
            raise HttpResponseBadRequest()
        try:
            article = Article.objects.get(pk = id)
        except Article.DoesNotExist:
            raise Http404
        return article

    def get(self, request, id, format=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorList(APIView):
    """
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/authors

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_object(self, id):
        try:
            id = int(id)
        except ValueError:
            raise HttpResponseBadRequest()
        try:
            author = Author.objects.get(pk = id)
        except Author.DoesNotExist:
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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        author = self.get_object(id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
