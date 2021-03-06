# Generated by Django 3.1.3 on 2021-01-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HighLight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nome da área')),
                ('title2', models.CharField(max_length=200, verbose_name='Nome do trabalho')),
                ('text', models.TextField(verbose_name='Texto')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='portfolio_posts/images', verbose_name='Imagem1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='portfolio_posts/images', verbose_name='Imagem2')),
            ],
        ),
    ]
