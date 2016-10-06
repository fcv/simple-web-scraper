from django.http import HttpResponse, Http404, HttpResponseRedirect


def articles(request):
    return HttpResponse('[{"id": 1, "title": "Fake Article"}]')
