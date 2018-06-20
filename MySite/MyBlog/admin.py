from django.contrib import admin
from MyBlog import models

class ArticleConfig(admin.ModelAdmin):
    list_display = ["title","created_time","category","quantity","stick"]

admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Article,ArticleConfig)