from django.contrib import admin

from .models import Projeto, GaleriaProjeto
# Register your models here.

class GaleriaProjetoClasse(admin.TabularInline):
	model = GaleriaProjeto
	extra = 0

class ProjetoAdmin(admin.ModelAdmin):
	list_display = ['proj_title', 'proj_slug', 'proj_published_date'] #o que será listado no admin
	search_fields = ['proj_title', 'proj_slug'] #buscas no admin
	prepopulated_fields = {'proj_slug': ('proj_title',)} #atalho slug a partir do título do post
	inlines=[GaleriaProjetoClasse,]

admin.site.register(Projeto, ProjetoAdmin)