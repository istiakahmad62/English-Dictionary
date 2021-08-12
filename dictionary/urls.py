from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('word-details', views.word_details, name="word"),
]
