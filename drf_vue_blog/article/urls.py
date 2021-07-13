from article.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path,include

urlpatterns = [
    path('article/',ArticleAPIView.as_view()),
]