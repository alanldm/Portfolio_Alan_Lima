from django.urls import include, path, re_path, reverse
from . import views

app_name = 'portfolio_posts'

urlpatterns = [
	path('', views.index, name='index'),
	path('prototipagem/<slug>', views.details_prototipagem, name='details_prototipagem'),
	path('artigo/<slug>', views.details_artigo, name='details_artigo'),
	path('apresentacao/<slug>', views.details_apresentacao, name='details_apresentacao'),
	path('projeto/<slug>', views.details_projeto, name='details_projeto'),
]