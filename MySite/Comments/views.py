from django.shortcuts import render,redirect,get_object_or_404,reverse
from MyBlog import models
from Comments.forms import CommentForm


def comments(request,blog_pk):
    article = get_object_or_404(models.Article,pk=blog_pk)
    if request.method == 'POST':
        # print(request.body)
        commentform = CommentForm(request.POST)


        if commentform.is_valid():
            # 校验通过，保存到数据库
            comment = commentform.save(commit=False)
            #绑定文章
            comment.article = article
            avatar = request.FILES.get("avatar")
            if not avatar:
                avatar = 'avatars/default.png'
            comment.avatar = avatar
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = {
                'article_obj':article,
                'commentform':commentform,
                'comment_list':comment_list,
            }
            return render(request,'MyBlog/detail.html',context=context)

    return redirect(models.Article)