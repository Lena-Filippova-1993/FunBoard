from django.contrib import admin

from .models import Post, Response

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'dateCreation']
    list_filter = ('author', 'dateCreation')

admin.site.register(Post, PostAdmin)
