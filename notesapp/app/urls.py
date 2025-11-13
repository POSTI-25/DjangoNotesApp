from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.list),
    path('app/<int:pk>/',views.detail),
]