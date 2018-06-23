from django.shortcuts import render, get_object_or_404, HttpResponse
from MyBlog import models
from Comments.forms import CommentForm
from django.db.models import Q
from utils import page
import markdown


def index(request):
    article_list = models.Article.objects.all().exclude(stick=True).order_by("-created_time")
    stick_article_list = models.Article.objects.filter(stick=True)
    current_page = request.GET.get('page')
    pager = page.Pagination(current_page=current_page, all_count=article_list.count(), base_url='/index/')
    article_list = article_list[pager.start:pager.end]
    page_html = pager.page_html()
    context = {
        "article_list": article_list,
        "page_html": page_html,
        "stick_article_list":stick_article_list
    }
    return render(request, 'MyBlog/index.html', context=context)


def about(request):
    return render(request, 'MyBlog/about.html')


def detail(request, pk):
    article_obj = get_object_or_404(models.Article, pk=pk)
    article_obj.quantity_raise()
    article_obj.body = markdown.markdown(article_obj.body,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])

    commentform = CommentForm()
    all_comment = article_obj.comment_set.all().order_by('-created_time')
    current_page = request.GET.get('page')
    page_obj = page.Pagination(current_page=current_page, all_count=all_comment.count(), base_url="/blog/%s" % (pk),
                               per_page_num=10)
    comment_list = all_comment[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    context = {
        'all_comment':all_comment,
        'article_obj': article_obj,
        'commentform': commentform,
        'comment_list': comment_list,
        'page_html': page_html
    }
    return render(request, 'MyBlog/detail.html', context=context)

def archives(request, year, month):
    article_list = models.Article.objects.filter(created_time__year=year,
                                                 created_time__month=month,
                                                 ).order_by('-created_time')
    return render(request, 'MyBlog/category.html', {'article_list': article_list})


def category(request, title):
    article_list = models.Article.objects.filter(category__name=title).order_by('-created_time')

    return render(request, 'MyBlog/category.html', {'article_list': article_list})


def tag(request, tag):
    article_list = models.Article.objects.filter(tags__name=tag).order_by('-created_time')
    context = {
        'article_list': article_list
    }
    return render(request, 'MyBlog/tag.html', context=context)


def search(request):
    key = request.GET.get('q')
    if request.is_ajax():
        return HttpResponse('/search/?q=' + key)
    article_list = models.Article.objects.filter(Q(title__icontains=key) or Q(body__icontains=key))

    return render(request, 'MyBlog/category.html', {'article_list': article_list})


def source(request):
    return render(request, 'MyBlog/sourcecode.html')


def archives_html(request):
    # {'2018-06-1':[obj1,obj2,obj3]}

    archive_list = models.Article.objects.dates('created_time', 'month', order='DESC')
    # 2018-06-01
    article_dic = {}

    for time in archive_list:
        year, month = str(time).split('-')[0:2]

        article_list = models.Article.objects.all().filter(created_time__year=year,
                                                           created_time__month=month, ).order_by('-created_time')
        article_dic[(str(time))] = article_list

    # for article in article_list:
    #         if time in article_dic:
    #             article_dic[str(time)].append(article)
    #         else:
    #             article_dic[str(time)] = [article,]
    # print(article_dic)
    context = {
        'archive_list': archive_list,
        'article_dic':article_dic
    }
    return render(request, 'MyBlog/archives.html', context=context)
