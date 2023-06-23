from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Reply
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='Заголовок:')
    wysiwyn_text = forms.CharField(widget=CKEditorWidget(), label='Обьявление')

    class Meta:
        model = Post
        fields = [
                   'title',
                   'category',
                   'wysiwyn_text',
        ]
        labels = {'category': _('Категория')}

    def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("description")
       if text is not None and len(text) < 20:
           raise ValidationError({
               "text": "Статья/новость не может быть менее 20 символов."
           })

       return cleaned_data


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = [
                   'reply',
                 ]
        labels = {'reply': _('Отклик'),}

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
