from django.urls import path
from . import views

urlpatterns = [
    path('add_rss_feed/', views.AddRSSFeedView.as_view(), name='add-rss-feed'),
]