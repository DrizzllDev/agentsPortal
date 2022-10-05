from django.db import models
from ckeditor.fields import RichTextField

class Categories(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Список категорий'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class EducationArticles(models.Model):
    title = models.CharField(max_length=70, verbose_name='Заголовок статьи')
    description =  models.CharField(max_length=250, verbose_name='Краткое описание статьи')
    text = RichTextField(verbose_name='Статья')
    categories = models.ForeignKey(Categories, on_delete = models.SET_NULL, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


