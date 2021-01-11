from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Projeto

# Create your views here.
def index(request):
    template_name = 'portfolio_posts/portfolio.html'
    projects = Projeto.objects.filter(proj_published_date__lte=timezone.now()).order_by('-proj_published_date')
    context = {
        'projects': projects, 
    }
    return render(request,template_name,context)

def details_projeto(request, slug):
	project = get_object_or_404(Projeto, proj_slug=slug)
	template_name = 'portfolio_posts/details_projeto.html'
	context = {
        'project': project
    }
	return render(request, template_name, context)

