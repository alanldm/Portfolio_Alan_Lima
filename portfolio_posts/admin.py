from django.contrib import admin

from .models import Apresentacao, Artigo, Eletronica, Programacao, Projeto
# Register your models here.
class ApresentacaoAdmin(admin.ModelAdmin):
	list_display = ['ap_title', 'ap_slug', 'ap_published_date'] #o que será listado no admin
	search_fields = ['ap_title', 'ap_slug'] #buscas no admin
	prepopulated_fields = {'ap_slug': ('ap_title',)} #atalho slug a partir do título do post

class ArtigoAdmin(admin.ModelAdmin):
	list_display = ['art_title', 'art_slug', 'art_published_date'] #o que será listado no admin
	search_fields = ['art_title', 'art_slug'] #buscas no admin
	prepopulated_fields = {'art_slug': ('art_title',)} #atalho slug a partir do título do post

class EletronicaAdmin(admin.ModelAdmin):
	list_display = ['el_title', 'el_slug', 'el_published_date'] #o que será listado no admin
	search_fields = ['el_title', 'el_slug'] #buscas no admin
	prepopulated_fields = {'el_slug': ('el_title',)} #atalho slug a partir do título do post

class ProgramacaoAdmin(admin.ModelAdmin):
	list_display = ['prog_title', 'prog_slug', 'prog_published_date'] #o que será listado no admin
	search_fields = ['prog_title', 'prog_slug'] #buscas no admin
	prepopulated_fields = {'prog_slug': ('prog_title',)} #atalho slug a partir do título do post

class ProjetoAdmin(admin.ModelAdmin):
	list_display = ['proj_title', 'proj_slug', 'proj_published_date'] #o que será listado no admin
	search_fields = ['proj_title', 'proj_slug'] #buscas no admin
	prepopulated_fields = {'proj_slug': ('proj_title',)} #atalho slug a partir do título do post

admin.site.register(Apresentacao, ApresentacaoAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Eletronica, EletronicaAdmin)
admin.site.register(Programacao, ProgramacaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)