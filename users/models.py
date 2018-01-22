from django.db import models

# Create your models here.
'''
  User 也是继承自 AbstractUser 抽象基类，而且仅仅就是继承了 AbstractUser，没有
对 AbstractUser 做任何的拓展。所以，如果我们继承 AbstractUser，将获得 User 的全
部特性，而且还可以根据自己的需求进行拓展


              写上我们自定义的用户模型代码：
'''
from django.contrib.auth.models import User

class Profile(models.Model):
    nickname = models.CharField(max_length=50,blank=True)

    user = models.OneToOneField(User)

'''
PS：如果你使用了 Profile 模式，你可能希望在创建 User 对象的时候同时也创建与之
关联的 Profile 对象。你可以使用 Django 的 Signal 实现这个需求。由于 Profile 模
式不是我们要介绍的重点内容，因此具体的实现细节请参照相关的文档，这里不再赘
述。
OK，自定义的 User 模型已经建立好了，接下来就是如何创建用户，即用户注册流程
了。

Django 用户系统内置了登录、修改密码、找回密码等视图，但是唯独用户注册的
视图函数没有提供，这一部分需要我们自己来写




'''