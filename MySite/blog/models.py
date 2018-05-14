from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

# 分类表
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=50)

    def __str__(self):
        return self.name
# 标签表
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=50)
    def __str__(self):
        return self.name

# 文章表
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    #文章标题
    title = models.CharField(null=False,max_length=50)
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=200)
    #文章创建时间
    created_time = models.DateTimeField()
    #文章最后修改时间
    modified_time = models.DateTimeField()
    #文章主体
    body = models.TextField()
    #文章分类
    category = models.ForeignKey(Category)
    #文章标签
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title

    def get_abs_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta():
        db_table = ''
