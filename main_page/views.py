from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
# Create your views here.
from .models import *
from .serializers import *


class BookApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
