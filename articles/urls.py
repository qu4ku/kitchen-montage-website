from django.urls import path

from . import views
from .rss import ArticleFeedPL, ArticleFeedEN


urlpatterns = [
	# EN
	path('articles/', views.articles_view, name='articles'),
	path('articles/<slug:slug>/', views.post_view, name='post'),

	# PL
	path('pl/artykuly/', views.articles_pl_view, name='articles-pl'),
	path('pl/artykuly/<slug:slug>/', views.post_pl_view, name='post-pl'),

	# RSS
	path('feed/pl/', ArticleFeedPL(), name='rss-pl'),
	path('feed/en/', ArticleFeedEN(), name='rss-en'),
]