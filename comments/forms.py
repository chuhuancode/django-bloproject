from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','text']

'''
model = Comment 表明这个表单对应的数据库模型是 Comment 类。fields = ['name', 
'email', 'url', 'text'] 指定了表单需要显示的字段，这里我们指定了 name、email、url、
text 需要显示

'''