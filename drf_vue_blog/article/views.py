from django.shortcuts import render
from rest_framework.decorators import api_view
from article.permissions import IsAdminUserOrReadOnly
from article.serializer import *
from article.models import *
from rest_framework.generics import (
    CreateAPIView,RetrieveUpdateDestroyAPIView,
    GenericAPIView, UpdateAPIView,
    RetrieveAPIView, ListAPIView,
    ListCreateAPIView,get_object_or_404,
    DestroyAPIView
)
# Create your views here.

class ArticleAPIView(ListCreateAPIView):
    queryset = Artical.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = ArticleSerializer


    # def get_queryset(self):
    #     user_id = self.request.user.id
    #     qs = self.queryset.filter(user_id=user_id)
    #     return qs

