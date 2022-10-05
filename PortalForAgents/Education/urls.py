from django.contrib import admin
from django.urls import path
from .views import allArticlesPage, article

urlpatterns = [
    path('', allArticlesPage, name='allArticlesEducation'),
    path('<int:pk>', article, name='articleEducation'),
]
