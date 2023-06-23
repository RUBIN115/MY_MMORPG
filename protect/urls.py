from django.urls import path
from .views import IndexView, ReplyByPost
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='reply_list'),
    path('protect/reply/<int:pk>/accept', views.accept_reply, name="accept_reply"),
    path('protect/reply/<int:pk>/delete', views.delete_reply, name="delete_reply"),
    path('protect/filter/<int:pk>', ReplyByPost.as_view(), name="reply_by_post"),
    path('protect/subscribe', views.subscribe, name="suscribe"),
]