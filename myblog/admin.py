from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
     list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# Register your models here.
from .models import Post, Category, Tag
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
