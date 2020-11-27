from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Apresentacao, Artigo, Eletronica, Programacao, Projeto
from django.db.models import Q

# Create your views here.
def index(request):
    template_name = 'portfolio_posts/portfolio.html'
    presentations = Apresentacao.objects.filter(ap_published_date__lte=timezone.now()).order_by('-ap_published_date')
    articles = Artigo.objects.filter(art_published_date__lte=timezone.now()).order_by('-art_published_date')
    eletronics = Eletronica.objects.filter(el_published_date__lte=timezone.now()).order_by('-el_published_date')
    programs = Programacao.objects.filter(prog_published_date__lte=timezone.now()).order_by('-prog_published_date')
    projects = Projeto.objects.filter(proj_published_date__lte=timezone.now()).order_by('-proj_published_date')
    context = {
        'presentations': presentations, 
        'articles': articles, 
        'eletronics': eletronics,
        'programs': programs, 
        'projects': projects, 
    }
    return render(request,template_name,context)
