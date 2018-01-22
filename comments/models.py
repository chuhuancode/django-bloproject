from django.db import models

# Create your models here.
'''
用户评论的数据必须被存储到数据库里，以便其他用户访问时 Django 能从数据库取
回这些数据然后展示给访问的用户，因此我们需要为评论设计数据库模型，这和设计
文章、分类、标签的数据库模型是一样的。
'''
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey("myblog.Post")

    def __str__(self):
        return self.text[:30]

'''
设计数据库字段，和HTML页面 中的前段代码要相互对应

然后根据表单的要求填写相应的数据。之后用户点击评论按钮，
这些数据就会发送给某个 URL。
'''






















