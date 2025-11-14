from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.NotesListView.as_view(), name = "notes.list"),
    path('app/<int:pk>/',views.NotesDetailView.as_view(), name = "notes.detail"),
    path('app/new', views.NotesCreateView.as_view(), name = "notes.new"),
]