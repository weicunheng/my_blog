from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
from .models import Category,Tag,Article
import markdown


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    return render(request, 'Blog/index.html', {'article_list':article_list})

def detail(request,pk):
    port = Article.objects.get(id=pk)
    port.body = markdown.markdown(port.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'Blog/detail.html', {'port':port})



#标签
def tags(request,tag):
    article_list = Article.objects.filter(tags__name=tag)
    return render(request, "Blog/tag.html", {"article_list": article_list})

# 分类
def category(request,classify):

    # article_list=Article.objects.filter(category__name=classify).order_by("-created_time")
    article_list=Article.objects.filter(category__name=classify)
    return render(request,"Blog/Category.html",{"article_list":article_list})


#归档
def archives(request,year,month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month,)

    return render(request,"Blog/archives.html",{'article_list':article_list})



def about(request):
    return render(request,'Blog/aboutme.html')