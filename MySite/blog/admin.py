from django.contrib import admin
from blog.models import Category,Tag,Article

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title','excerpt', 'created_time', 'modified_time', 'category', 'tags']

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)