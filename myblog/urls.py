from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
app_name  = 'myblog'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name= 'index'),
    #url(r'detail/$',views.detail,name = 'datail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    #限制访问的路由,当点击某一篇文章的时候，要展示文章详情页的时候！！！如果没有登陆，
    #限制访问，所以限制的是访问某一篇文章时候的视图函数
    #url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$',login_required(views.PostDetailView.as_view()),name='detail'
),

]
'''
而当用户访问 <网站域名>/post/2/ 时，显示的是第二篇文章的内容，这里数字代表了第几篇文
章，也就是数据库中 Post 记录的 id 值。
被括起来的部分 (?P<pk>[0-9]+)匹配 255，
那么这个 255 会在调用视图函数 detail 时被传递进去给到参数 pk，实际上视图函数
的调用就是这个样子：detail(request, pk=255)。我们这里必须从 URL 里捕获文章的
id，因为只有这样我们才能知道用户访问的究竟是哪篇文章。

'''