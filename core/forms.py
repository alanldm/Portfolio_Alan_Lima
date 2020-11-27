from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template

class ContactMessage(forms.Form):

	name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Nome'}))
	email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'E-mail'}))
	about = forms.CharField(label='Assunto do e-mail', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Assunto do e-mail'}))
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Mensagem'}))

	def send_mail(self):
		subject = self.cleaned_data['about']
		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
		}
		template_name = 'core/contact_email.html'
		send_mail_template(subject, template_name, context, 
			[settings.CONTACT_EMAIL]
		)