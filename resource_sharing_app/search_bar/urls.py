# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.search_view, name='search_view'),
]
