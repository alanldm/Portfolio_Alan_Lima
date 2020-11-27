from django.urls import include, path, re_path, reverse
from . import views

app_name = 'portfolio_posts'

urlpatterns = [
	path('', views.index, name='index'),
]