import django_filters
from django_filters import FilterSet
from django.utils.translation import gettext_lazy as _
from board.models import Reply, Post


# Создаем свой набор фильтров для модели Post.
class ReplyFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['title',]
        labels = {'title': _('Обьявление')}

