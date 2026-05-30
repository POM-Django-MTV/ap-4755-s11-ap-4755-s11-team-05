from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_page, name='author_page'),
]