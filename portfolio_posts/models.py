from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Projeto(models.Model):
    proj_title = models.CharField('Título', max_length=200)
    proj_slug = models.SlugField('Atalho')
    proj_area = models.CharField('Área', max_length=100, null=True, blank=True)
    proj_text = models.TextField('Texto')
    proj_img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True)
    proj_published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.proj_title

    def get_absolute_url_proj(self):
        return reverse('portfolio_posts:details_projeto', args=[str(self.proj_slug)])

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['proj_published_date']

class GaleriaProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="Imagem_projeto", null=True, blank=True)
    imagem = models.ImageField('Imagem', upload_to='portfolio_posts/images', blank=True, null=True)
    title = models.CharField('Título da imagem', max_length=100, blank=True, null=True)

