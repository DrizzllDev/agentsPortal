from django.shortcuts import render
from django.http import HttpResponse
from .models import EducationArticles


def allArticlesPage(request):
    allArticles = EducationArticles.objects.all()
    return render(request, 'Education/all_articles.html', {'allArticles':allArticles})


def article(request, pk):
    getArticle = EducationArticles.objects.get(pk=pk)
    return render(request, 'Education/article.html', {'article': getArticle})

