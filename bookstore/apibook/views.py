from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from apibook.serializers import BookSerializer
from apibook.models import Book

class ListBookAPIView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CreateBookAPIView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class UpdateBookAPIView(UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class DeleteBookAPIViwe(DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  