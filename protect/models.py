from django.db import models
from ckeditor.fields import RichTextField

# Модель новостной рассылки.
# Рассылка последней добавленной новости по сигналу сохранения модели и если флаг Черновик сброшен
class NewsToSend(models.Model):
    date_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    wysiwyn_text = RichTextField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'