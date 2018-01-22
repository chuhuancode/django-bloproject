from  django import template
from ..models import Post,Category

'''
这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将
函数 get_recent_posts 装饰为 register.simple_tag。这样就可以在模板中使用语法 {% 
get_recent_posts %} 调用这个函数了
'''

register = template.Library()

@register.simple_tag()
def get_recent_post(num = 5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time','month',order='DESC')


@register.simple_tag()
def get_categories():
    return Category.objects.all()










