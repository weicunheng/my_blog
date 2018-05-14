from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
from .models import Category,Tag,Article
import markdown


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    # print('article_list',article_list)
    # print('tag:>>>>>',article_list[0].tags)
    return render(request, 'Blog/index.html', {'article_list':article_list})

def detail(request,pk):
    port = Article.objects.get(id=pk)
    port.body = markdown.markdown(port.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,'Blog/detail.html',{'port':port})

def about(request):
    return render(request,'Blog/aboutme.html')