from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50,default = 'articles title',verbose_name = 'نینر')
    description = models.TextField(max_length=250,default = 'articles description',verbose_name = 'توصیفات')
    thumbnail = models.ImageField(null = True,blank = True,verbose_name = 'عکس')
    created_at = models.DateTimeField(default = timezone.now,verbose_name = 'تاریخ و ساعت')
    

    def __str__(self):
        return self.title 