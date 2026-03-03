from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'views_count')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)