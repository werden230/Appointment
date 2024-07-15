from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def info(request):
    return HttpResponse("<h1>Main Page</h1>")


def blog(request):
    return HttpResponse("<h1>Blog</h1>")


def post(request, post_id):
    return HttpResponse(f"<h1>Blog</h1><p>Post №{post_id}</p>")


def error404(request, exception):
    return HttpResponseNotFound("<h1>n0t f0und =(</h1>")