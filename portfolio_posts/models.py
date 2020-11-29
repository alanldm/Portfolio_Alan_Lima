from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Apresentacao(models.Model):
    ap_title = models.CharField('Título', max_length=200)
    ap_slug = models.SlugField('Atalho')
    ap_text = models.TextField('Texto')
    ap_img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True)
    ap_img2 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem2', null=True, blank=True )
    ap_img3 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem3', null=True, blank=True )
    ap_published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ap_title

    def get_absolute_url(self):
        return reverse('portfolio_posts:details_apresentacao', args=[str(self.ap_slug)])

    class Meta:
        verbose_name = 'Apresentação'
        verbose_name_plural = 'Apresentações'
        ordering = ['ap_published_date']

class Artigo(models.Model):
    art_title = models.CharField('Título', max_length=200)
    art_slug = models.SlugField('Atalho')
    art_text = models.TextField('Texto')
    art_img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True )
    art_img2 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem2', null=True, blank=True )
    art_img3 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Certificado Apresentação', null=True, blank=True )
    art_published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.art_title

    def get_absolute_url(self):
        return reverse('portfolio_posts:details_artigo', args=[str(self.art_slug)])

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['art_published_date']

class Eletronica(models.Model):
    el_title = models.CharField('Título', max_length=200)
    el_slug = models.SlugField('Atalho')
    el_text = models.TextField('Texto')
    el_img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True )
    el_img2 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem2', null=True, blank=True )
    el_img3 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem3', null=True, blank=True )
    el_img4 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem3', null=True, blank=True )
    el_img5 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem3', null=True, blank=True )
    el_published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.el_title

    def get_absolute_url(self):
        return reverse('portfolio_posts:details_prototipagem', args=[str(self.el_slug)])

    class Meta:
        verbose_name = 'Eletrônica'
        verbose_name_plural = 'Eletrônicas'
        ordering = ['el_published_date']

class Projeto(models.Model):
    proj_title = models.CharField('Título', max_length=200)
    proj_slug = models.SlugField('Atalho')
    proj_text = models.TextField('Texto')
    proj_img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True )
    proj_img2 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem2', null=True, blank=True )
    proj_img3 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem3', null=True, blank=True )
    proj_published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.proj_title

    def get_absolute_url(self):
        return reverse('portfolio_posts:details_projeto', args=[str(self.proj_slug)])

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['proj_published_date']

