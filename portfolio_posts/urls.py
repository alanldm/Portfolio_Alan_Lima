from django.urls import include, path, re_path, reverse
from . import views

app_name = 'portfolio_posts'

urlpatterns = [
	path('', views.index, name='index'),
	re_path('(?P<slug>[\w_-]+)/', views.details_prototipagem, name='details_prototipagem'),
	re_path('(?P<slug>[\w_-]+)/', views.details_artigo, name='details_artigo'),
	re_path('(?P<slug>[\w_-]+)/', views.details_apresentacao, name='details_apresentacao'),
	re_path('(?P<slug>[\w_-]+)/', views.details_projeto, name='details_projeto'),
]