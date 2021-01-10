from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статья')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_release = models.DateTimeField()

    class Meta:
        ordering = ('-date_release',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



    def __str__(self):
        return self.title

