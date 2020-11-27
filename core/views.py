from django.shortcuts import render, get_object_or_404
from .forms import ContactMessage
from django.urls import reverse

# Create your views here.
def index(request):
    template_name = 'core/index.html'
    if request.method == 'POST':
        form = ContactMessage(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = ContactMessage()
    else:
        form = ContactMessage()
    context = {
        'form': form,
    }
    return render(request,template_name)
