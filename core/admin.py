from django.contrib import admin
from .models import HighLight

# Register your models here.
class H_admin(admin.ModelAdmin):
	list_display = ['title', 'title2'] 
	search_fields = ['title', 'title2']
	prepopulated_fields = {'slug': ('title',)} #atalho slug a partir do título do post 

admin.site.register(HighLight, H_admin)