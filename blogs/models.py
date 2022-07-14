from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
