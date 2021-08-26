from django.urls import path
from apibook import views

urlpatterns = [
  path("", views.ListBookAPIView.as_view(), name="book_list"),
  path("create/", views.CreateBookAPIView.as_view(), name="book_create"),
  path("update/<int:pk>/", views.UpdateBookAPIView.as_view(), name="book_update"),
  path("delete/<int:pk>/", views.DeleteBookAPIViwe.as_view(), name="book_delete")
]