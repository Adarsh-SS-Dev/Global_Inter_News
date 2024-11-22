from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import ContactMessage
 
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','heading','category','date','slug','tags')

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','cmt','date')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)

