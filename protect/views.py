from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import ReplyFilter
from board.models import Reply, Post, SubscribedUsers


#вью приватной страницы
class IndexView(LoginRequiredMixin, ListView):
    #login_url = '/sign/login'
    #redirect_field_name = 'redirect_to'
    model = Reply
    template_name = 'protect/index.html'
    context_object_name = 'reply_list'
    ordering = '-date_time_in'
    paginate_by = 6

    # Переопределяем функцию получения списка откликов
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ReplyFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #добавим данных: отклики, подписан ли на новости
        context['reply_list'] = Reply.objects.filter(user=self.request.user.id).order_by('-date_time_in')
        context['is_not_subscribed'] = False if SubscribedUsers.objects.filter(user=self.request.user.id).exists() else True
        return context


class ReplyByPost(LoginRequiredMixin, ListView):
    model = Reply

    template_name = 'protect/replys_by_post.html'
    ordering = '-date_time_in'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reply_list_by_postid = Reply.objects.filter(post=self.kwargs['pk']).order_by('-date_time_in')
        post = Post.objects.get(id=self.kwargs['pk'])
        #print(reply_list_by_postid)
        context['reply_list'] = reply_list_by_postid
        context['post'] = post
        return context


#принять отклик
@login_required
def accept_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    if reply:
        reply.accepted = True
        reply.save(update_fields=['accepted'])

    #Возвращаемся на страницу, откуда перешли
    return redirect(request.META.get('HTTP_REFERER'))


#удаляем отклик
@login_required
def delete_reply(request, pk):
    Reply.objects.get(id=pk).delete()
    # Возвращаемся на страницу, откуда перешли
    return redirect(request.META.get('HTTP_REFERER'))


#подписка на новости
@login_required
def subscribe(request):
    subscribe = SubscribedUsers()
    subscribe.user = request.user
    subscribe.save()
    # Возвращаемся на страницу, откуда перешли
    return redirect(request.META.get('HTTP_REFERER'))
