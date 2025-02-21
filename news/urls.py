from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page , name='news_page'),
    path('<int:article_id>/', views.article_content, name="article_content"),
    path('add/', views.add_article, name="add_article"),
    path('edit/<int:article_id>/', views.edit_article, name="edit_article"),
    path('delete/<int:article_id>/', views.delete_article, name="delete_article")
]
