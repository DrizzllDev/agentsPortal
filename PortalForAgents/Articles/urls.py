from django.urls import path
from .views import allArticlesPage, article

urlpatterns = [
    path('', allArticlesPage, name='allArticles'),
    path('<int:pk>', article, name='article'),
]
