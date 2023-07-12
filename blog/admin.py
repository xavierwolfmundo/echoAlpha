from django.contrib import admin
from .models import Category, Tag, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    list_filter = ['date_posted', 'author', 'categories', 'tags']
    search_fields = ['title', 'content']
    date_hierarchy = 'date_posted'
    ordering = ['-date_posted']

    filter_horizontal = ['categories', 'tags']
