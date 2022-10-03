from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def allArticlesPage(request):
    allArticles = Articles.objects.all()
    return render(request,'Articles/all_articles.html',{'allArticles':allArticles})


def article(request, pk):
    article = Articles.objects.get(pk=pk)
    return render(request, 'Articles/article.html', {'article': article})

