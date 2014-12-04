from django.contrib import admin

from models import Blog,Step
from django.contrib.admin.templatetags.admin_list import date_hierarchy

class AdminBlog(admin.ModelAdmin):
    list_display = ('title','author','datetime','category')
    search_fields = ('title','author','category')
    list_filter = ("datetime",)
    #date_hierarchy = 'datetime'
     
admin.site.register(Blog,AdminBlog)
