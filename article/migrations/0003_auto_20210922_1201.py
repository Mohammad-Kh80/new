# Generated by Django 3.2.7 on 2021-09-22 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default='articles description', max_length=250),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='articles title', max_length=50),
        ),
    ]