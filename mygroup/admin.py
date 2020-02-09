from django.contrib import admin
from mygroup.models import Post
from mygroup.models import Category

admin.site.register(Post)
admin.site.register(Category)