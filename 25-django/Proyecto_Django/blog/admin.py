from typing import Any
from django.contrib import admin
from .models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_username', 'get_category_names', 'public', 'created_at', 'update_at')
    list_filter = ('public', 'created_at', 'update_at', 'categories')
    search_fields = ('title', 'user__username', 'categories__name')
    readonly_fields = ('created_at', 'update_at')
    filter_horizontal = ('categories',)
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_category_names(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
            
        obj.save()
    
    get_username.short_description = 'Usuario'
    get_category_names.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
 