from django.contrib import admin
from .models import Post # makes the Post model visible on admin page

# Register your models here.
admin.site.register(Post)