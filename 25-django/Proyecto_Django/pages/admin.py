from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']  # Puedes incluir otros campos también, como 'title' o 'order'.
    search_fields = ('title', 'content')
    list_filter = ('visible', )
    list_display =('title', 'visible', 'created_at')
    ordering = ('created_at', )
    
    
admin.site.register(Page, PageAdmin)

# Register your models here.



#Configuracion del panel
title = "Proyecto de Django"
subtitle = "Panel de gestion"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
