from django.forms import ModelForm,TextInput,EmailInput,URLInput,Textarea,FileInput
from MessageBoard import models

class MessageBoardForm(ModelForm):
    class Meta:
        model = models.Message
        fields=['name','email','url','content','avatar']
        widgets = {
            'name': TextInput(attrs={'class':"form-control",'placeholder':"nickname"}),
            'email': EmailInput(attrs={'class':"form-control",'placeholder':"email@xx.com"}),
            'url': URLInput(attrs={'class':"form-control",'placeholder':"your blog"}),
            'content': Textarea(attrs={'class':"form-control",'placeholder':"留言越屌,bug越少",'style':"resize:none",'rows':"5"}),
            'avatar': FileInput(attrs={'accept': 'image/*', 'onchange': 'verificationPicFile(this)'})

        }
        error_messages = {
            'name': {
                'required': '用户名不能为空',
                'max_length': ("您输入的昵称过长。"),
            },
            'email': {
                'required': '邮箱不能为空',
                'max_length': ("您输入的邮箱地址过长。"),
                'invalid': '您输入的邮箱格式不正确',
            },
            'url': {
                'max_length': ("您输入的博客地址过长。"),
                'invalid':'您输入的URL格式不正确',
            },
            'content': {
                'max_length': ("您输入的评论内容超出限制。"),
            },
        }
