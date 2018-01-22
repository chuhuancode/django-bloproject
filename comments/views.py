from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from myblog.models import Post
from.models import Comment
from .forms import CommentForm

def post_comment(requrst,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    if requrst.method =='POST':
# 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了
        form = CommentForm(requrst.POST)

        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                       }
            return render(requrst,'myblog/detail.html',context=context)

'''
  有两处地方显示的评论量，显示评论量的方法很简单。回顾一下我们是如何获取某
篇 post 的下的评论列表的？我们使用的是 post.comment_set.all()。all 方法返回
该 post 关联的评论列表。此外模型管理器（comment_set 是一个特殊的模型管理器）还
有一个 count 方法，返回的是数量，即 post 下有多少条评论，我们可以直接在模板中
调用这个方法：{{ post.comment_set.count }}。将评论量替换成该模板变量就可以正
确显示文章的评论数了。

'''