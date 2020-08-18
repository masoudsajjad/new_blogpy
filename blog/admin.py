from django.contrib import admin
from .models import *


class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, AdminUserProfile)


class AdminArticle(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'created_at', 'category', 'author']


admin.site.register(Article, AdminArticle)


class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(Category, AdminCategory)

