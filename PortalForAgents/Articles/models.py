from django.db import models
from ckeditor.fields import RichTextField


class Articles(models.Model):
    title = models.CharField(max_length=70, verbose_name="Заголовок статьи")
    description = models.CharField(max_length=250, verbose_name="Краткое описание статьи")
    text = RichTextField(verbose_name="Статья")

    class Meta:
        verbose_name = "Список статей"
        verbose_name_plural = "Список статей"

    def __str__(self):
        return self.title