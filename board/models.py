from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from ckeditor.fields import RichTextField #wysiwyn редактор
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    date_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    wysiwyn_text = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def preview(self):
        return self.text[:124] + "..."

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title} | {self.author}'


#Модель подписанных на рассылку пользователей
class SubscribedUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Reply(models.Model):
    date_time_in = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()
    accepted = models.BooleanField(default=False)  # True - принят, False - по умолчанию
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reply}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.post.id)])
