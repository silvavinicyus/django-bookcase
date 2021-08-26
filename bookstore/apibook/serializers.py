from django.db.models import fields
from rest_framework import serializers
from apibook.models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = "__all__"