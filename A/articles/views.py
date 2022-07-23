
from articles.models import Article
from .forms import ArticleForm , SefareshForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render  
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages

@login_required
def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()

    articles = Article.objects.filter(is_active = True)
    context ={
        'articles': articles, 
        'form': form
    }

    return render (request,'index.html', context)




def retrieve(request,id):
    articles = Article.objects.get(id=id)
    if request.method == "POST":
        form = SefareshForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SefareshForm()
        
    context ={
        'articles':articles,
        'form':form,
    }
    return render(request,'retrieve.html',context)


