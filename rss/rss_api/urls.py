from django.urls import path
from . import views

urlpatterns = [
    path('rssfeeds/', views.RSSFeedListCreateView.as_view(), name='rssfeed-list-create'),
    path('rssfeeds/<int:pk>/', views.RSSFeedDetailView.as_view(), name='rssfeed-detail'),
    path('selectedfeeds/', views.SelectedFeedListCreateView.as_view(), name='selectedfeed-list-create'),
    path('selectedfeeds/<int:pk>/', views.SelectedFeedDetailView.as_view(), name='selectedfeed-detail'),
]