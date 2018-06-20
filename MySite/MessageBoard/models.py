from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=32,null=True,blank=True)
    url = models.URLField(max_length=50,null=True,blank=True)
    content = models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(to='self',null=True,blank=True)
    avatar = models.ImageField(upload_to="boardavatars/", default="boardavatars/default.png",blank=True,null=True)


    def __str__(self):
        return self.name + self.content

    class Meta:
        db_table='message'
