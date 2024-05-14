from django.shortcuts import render
from .models import News
import requests

# Create your views here.

# newss = [
#     {'id':1, 'name':"Hello"},
#     {'id':2, 'name':"Hello World"},
#     {'id':3, 'name':"Bye World"},
# ]

def home (request):
    newss = News.objects.all()
    context = {'newss' : newss}
    return render(request, 'base/home.html', context)

def news(request, pk):
    news = News.objects.get(id = pk)
    context = {'news': news}
    return render(request, 'base/news.html', context )


def times1(request):
    context = {'response': response}
    response = request.get('https://newsapi.org/v2/everything?q=tesla&from=2024-04-13&sortBy=publishedAt&apiKey=0d4e2dad1ec84f608975e2af2fb497c9').json()
    return render(request, 'base/home.html', context)
print('response')
def times2(request):
    context = {'response': response}
    response = request.get('https://newsapi.org/v2/everything?q=apple&from=2024-05-12&to=2024-05-12&sortBy=popularity&apiKey=0d4e2dad1ec84f608975e2af2fb497c9').json()
    return render(request, 'base/home.hmtl', context)

def times3(request):
    context = {'response': response}
    response = request.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0d4e2dad1ec84f608975e2af2fb497c9').json()
    return render(request, 'base/home.hmtl', context)

def times4(request):
    context = {'response': response}
    response = request.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0d4e2dad1ec84f608975e2af2fb497c9').json()
    return render(request, 'base/home.hmtl', context)

