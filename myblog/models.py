from django.core.urlresolvers import reverse
from django.db import models

from django.contrib.auth.models import User
#from django.urls import reverse
#from django.contrib import *


#from users.models import User
#文章（Post）、分类（Category）以及标签（Tag）
# 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对
#多的关联关系，和 Category 类似。author = models.ForeignKey(User)
from django.shortcuts import redirect


class Category(models.Model):
    name = models.CharField(max_length=64)

class Tag(models.Model):
    name = models.CharField(max_length=64)

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=256,blank=True)
# created_time、modified_time。这两个列分别表示文章的创建时间和最后一次修
# 改时间，存储时间的列用DateTimeField数据类型
#关系-----------
# 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

    views =models.PositiveIntegerField(default=0)
#这里我们通过 ForeignKey 把文章和 User 关联了起来，
#因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是
#一对多的关联关系，和 Category 类似.

    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={"pk":self.pk})
#这个方法到底是怎么写出来的呢   还有 pk = id ???
# 在 urls.py 中加上了app_name = 'myblog',,,所以这里也要加上‘myblog’

    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])
'''
  increase_views 方法首先将自身对应的 views 字段
的值 +1（此时数据库中的值还没变），然后调用 save 
方法将更改后的值保存到数据库。注意这里使用了 update_fields 
参数来告诉 Django 只更新数据库中 views 字段的值，以提高

'''

'''
context_object_name————在模板中的变量名。{{name}}
template_name————-模板一般是一个html文件名
paginate_by————如果做分页这个参数说明每页有几个item项
model——————对应的模型（Model）
http_method_names———-请求类型 可以是get或者post

'''











'''
超级用户：963.
密码：963.8520

'''