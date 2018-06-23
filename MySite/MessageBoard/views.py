from django.shortcuts import render,redirect
from MessageBoard.forms import MessageBoardForm
from MessageBoard import models
from utils.page import Pagination


def message_board(request):
    messageboardform = MessageBoardForm()
    if request.method == 'POST':
        messageboardform = MessageBoardForm(request.POST)
        if messageboardform.is_valid():
            # 校验通过，保存到数据库
            form = messageboardform.save(commit=False)
            #绑定文章
            avatar = request.FILES.get("avatar")
            if not avatar:
                avatar = 'avatars/default.png'
            form.avatar = avatar
            form.save()
            return redirect('/message/')
        else:
            print('error',request.POST)
            print(messageboardform.errors)
            message_list = models.Message.objects.all()
            context = {
                'messageboardform':messageboardform,
                'comment_list':message_list,
            }
            return render(request,'MyBlog/message_board.html',context=context)
    all_message = models.Message.objects.all().order_by('-created_time')
    current_page = request.GET.get('page')
    page_obj = Pagination(current_page=current_page,all_count=all_message.count(),base_url='/message/',per_page_num=10)
    message_list = all_message[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    context = {
        'all_message':all_message,
        'messageboardform':messageboardform,
        'message_list':message_list,
        'page_html':page_html,
    }
    return render(request,'MyBlog/message_board.html',context=context)