from django.db import models
from django.conf import settings

class HighLight(models.Model):
    title = models.CharField('Nome da área', max_length=200)
    slug = models.SlugField('Atalho')
    title2 = models.CharField('Nome do trabalho', max_length=200)
    text = models.TextField('Texto')
    img1 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem1', null=True, blank=True)
    img2 = models.ImageField(upload_to='portfolio_posts/images', verbose_name='Imagem2', null=True, blank=True )

    def __str__(self):
        return self.title
