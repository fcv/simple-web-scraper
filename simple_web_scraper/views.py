from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.db.models import Q
from django.shortcuts import render
from articles.models import Author, AuthorSerializer, Article, ArticleSerializer, Outlet, OutletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


class OutletList(APIView):
    """
    Handles REST API request to outlet endpoint, more specifically the one performed to its root folder
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        outlets = Outlet.objects.all().order_by('-id')
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = OutletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def articles(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'articles.html', {
        'articles': articles,
        'active_menu': 'articles',
    })


class ArticleList(APIView):
    """
    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get(self, request, format = None):
        articles = Article.objects.all().order_by('-id')
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


class OutletDetail(APIView):
    """
    Handles REST API request to Outlet's endpoint, more specifically ones related to a single instance manipulation.
    Example: GET http://hostname/api/rest/v1/outlet/1

    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get_object(self, id):
        try:
            id = int(id)
        except ValueError:
            raise HttpResponseBadRequest()
        try:
            outlet = Outlet.objects.get(pk = id)
        except Article.DoesNotExist:
            raise Http404
        return outlet

    def get(self, request, id, format=None):
        outlet = self.get_object(id)
        serializer = OutletSerializer(outlet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        outlet = self.get_object(id)
        serializer = OutletSerializer(outlet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        outlet = self.get_object(id)
        outlet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleDetail(APIView):
    """
    Handles REST API request to Article's endpoint.

    Class-based Views based on django rest framework documentation.

    This class handles GET and POST request to root endpoint address.
    Example: GET http://hostname/rest/api/v1/article

    see http://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

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
        authors = Author.objects.all().order_by('-id')
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
