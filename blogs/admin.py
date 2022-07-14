from django.contrib import admin

# Register your models here.
from blogs.models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date_added')
    list_filter = ('date_added',)


admin.site.register(BlogPost, BlogPostAdmin)
