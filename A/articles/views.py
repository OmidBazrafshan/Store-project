
from articles.models import Article
from .forms import ArticleForm , SefareshForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View



@login_required

class IndexView(View):

    def get(self, request,*args,**kwargs):
        form = ArticleForm(request.POST,request.FILE)
        articles = Article.objects.filter(is_active = True)
        context ={
            'articles': articles, 
            'form': form
        }
        
        return render (request,'index.html', context)
    
    def post(self, request,*args,**kwargs):

        if form.is_valid():
            form.save()
        else:
            form = ArticleForm()
        return redirect("Home")



class RetrieveView(View):

    def get(self, request,*args,**kwargs):
        articles = Article.objects.get(id=id)
        form = SefareshForm(request.POST)
        context ={
            'articles':articles,
            'form':form
        }
        return render(request,'retrieve.html',context)

    def post(self, request,*args,**kwargs):
        if form.is_valid():
            form.save()
        else:
            form = SefareshForm()

        return redirect("Retrive")




        



