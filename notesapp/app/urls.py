from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.NotesListView.as_view()),
    path('app/<int:pk>/',views.NotesDetailView.as_view()),
]