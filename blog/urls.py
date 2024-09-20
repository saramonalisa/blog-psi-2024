from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/id', views.postagem, name='post')
]