# Generated by Django 3.1.3 on 2021-01-11 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_posts', '0008_projeto_proj_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='proj_area',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Área'),
        ),
    ]
