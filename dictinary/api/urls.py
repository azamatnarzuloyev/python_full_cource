from django.urls import path
from . import views

urlpatterns = [
  
    path("worlds/", views.WorldListViews.as_view(), name="Worlds-list"),
    path('detail/<slug>/', views.WorldDetailView.as_view(), name="worlds-detail"),
    path('search/', views.WorldSearch.as_view(), name="words-search"),
]