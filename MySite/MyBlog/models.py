from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
import markdown


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table="category"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table="tag"

class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    #是否是置顶
    stick=models.BooleanField()
    quantity = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={'pk':self.pk})

    def quantity_raise(self):
        self.quantity += 1
        self.save(update_fields=['quantity'])

    def save(self,*args,**kwargs):

        #如果没有填写摘要,自动生成摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            body = md.convert(self.body)
            soup = BeautifulSoup(body,'html.parser')
            self.excerpt = soup.text[:54]
        super(Article,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table="article"