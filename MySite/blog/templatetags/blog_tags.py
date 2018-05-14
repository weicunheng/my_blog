from django import template
from blog.models import Article,Category,Tag
from django.db.models import Count

register = template.Library()


# 获取最新文章的filter
@register.simple_tag
def get_new_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]

#归档filter：根据时间进行分类
@register.simple_tag
def get_archives():
    # select * from article group by create_time
    # return Article.objects.values().annotate('created_time').all()
    return Article.objects.dates('created_time', 'month', order='DESC')

#分类filter
@register.simple_tag
def get_classify():
    return Category.objects.all()

# tags
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('name')).filter(num_posts__gt=0)