from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from  .models import  Post,Category
from comments.forms import CommentForm

'''
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'myblog/index.html',context={"post_list":post_list})
这代码的作用：连接数据库 和 HTML页面展示页
Post.objects.all() 这个方法从数据库中去出来，所有的存在数据库中的文章
在admin后台中 post中写文章，保存以后就直接存到了数据库中
'''
#    model：将 model 指定为 Post，告诉 Django 我要获取的模型是 Post。
# • template_name：指定这个视图渲染的模板。
# • context_object_name：指定获取的模型列表数据保存的变量名。这个变量会被
# 传递给模板。
from django.views.generic import ListView
class IndexView(ListView):
    model = Post
    template_name = 'myblog/index.html'
    context_object_name = 'post_list'



'''
def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list}
    return render(request, 'myblog/detail.html', context=context)

   视图函数很简单，它根据我们从 URL 捕获的文章 id（也就是 pk，这里 pk 和 id 是等
价的）获取数据库中文章 id 为该值的记录，然后传递给模板。注意这里我们用到了从
django.shortcuts 模块导入的 get_object_or_404 方法，其作用就是当传入的 pk 对应的
Post 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错
误，表明用户请求的文章不存在。

------------------------------------------------------------------------------
    紧接着我们覆写了 get 方法。这对应着 detail 视图函数中将 post 的阅读量 +1 的
那部分代码。事实上，你可以简单地把 get 方法的调用看成是 detail 视图函数的调
用。
    接着我们又复写了 get_object 方法。这对应着 detail 视图函数中根据文章的 id（也
就是 pk）获取文章，然后对文章的 post.body 进行 Markdown 渲染的代码部
分。
    最后我们复写了 get_context_data 方法。这部分对应着 detail 视图函数中生成评论表
单、获取 post 下的评论列表的代码部分。这个方法返回的值是一个字典，这个字
典就是模板变量字典，最终会被传递给模板。
    你也许会被这么多方法搞乱，为了便于理解，你可以简单地把 get 方法看成
是 detail 视图函数，至于其它的像 get_object、get_context_data 都是辅助方法，这
些方法最终在 get 方法中被调用，这里你没有看到被调用的原因是它们隐含在
了 super(PostDetailView, self).get(request, *args, **kwargs) 即父类 get 方法的调用中。
    最终传递给浏览器的 HTTP 响应就是 get 方法返回的 HttpResponse 对象。
这些方法的相同点：都执行了父类方法，然后对父类方法的返回值进行一些操作，
最后返回这个修改后的返回值。
'''
# 此外我们可以看到 CategoryView 类中指定的属性值和 IndexView 中是一模一样的，
# 所以如果为了进一步节省代码，甚至可以直接继承 IndexView：
from django.views.generic import DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/detail.html'
    context_object_name = 'post'
    def get(self,request,*args,**kwargs):
        response =super(PostDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response
    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        return post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context
'''
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month ).order_by('-created_time')
    return render(request, 'myblog/index.html', context={'post_list': post_list})
'''
class ArchivesView(IndexView):
    def get_queryset(self):
        return super(ArchivesView,self).get_queryset().filter(
            created_time__year = self.kwargs.get('year'),
            created_time__month = self.kwargs.get('month')
        )




'''
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'myblog/index.html', context={'post_list': post_list})

这里我们首先根据传入的 pk 值（也就是被访问的分类的 id 值）从数据库中获取到这
个分类。get_object_or_404 函数和 detail 视图中一样，其作用是如果用户访问的分类不
存在，则返回一个 404 错误页面以提示用户访问的资源不存在。然后我们通
过 filter 函数过滤出了该分类下的全部文章。同样也和首页视图中一样对返回的文章列
表进行了排序。

显示在主页中， 因为只有当现实一篇文章的时候，才用到 detail 模板；
'''
class CategoryView(IndexView):
    model = Post
    template_name = 'myblog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category = cate)
