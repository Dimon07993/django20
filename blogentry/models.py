from django.db import models
from parso.python.tree import Class


class Blogentry(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, unique=True, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title