from django.forms import ModelForm,TextInput,EmailInput,URLInput,Textarea,ImageField
from Comments import models

#attrs={'class':"head-portrait",'title':"上传头像"}
class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields=['name','email','url','content','avatar']
        widgets = {
            'name': TextInput(attrs={'class':"form-control",'placeholder':"nickname"}),
            'email': EmailInput(attrs={'class':"form-control",'placeholder':"email@xx.com"}),
            'url': URLInput(attrs={'class':"form-control",'placeholder':"your blog"}),
            'content': Textarea(attrs={'class':"form-control",'placeholder':"看完不留一发？",'style':"resize:none",'rows':"5"}),
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
            },
            'content': {
                'max_length': ("您输入的评论内容超出限制。"),
            },
        }
