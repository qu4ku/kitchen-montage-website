from django.urls import path, include

from . import views


urlpatterns = [
	path('', views.home_mvp_view, name='home'),
]