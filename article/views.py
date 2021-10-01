from django.shortcuts import render
from .models import Article

def Home(request):
    article = Article.objects.all()
    return render(request,'article/home.html',context = {'article' : article})