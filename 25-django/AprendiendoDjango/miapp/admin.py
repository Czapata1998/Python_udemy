from django.contrib import admin
from.models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)


#Configurar el titulo del panel
admin.site.site_header = "Master en python - Cristhian Zapata"
admin.site.site_title = "Master en python - Cristhian Zapata"
admin.site.index_title = "Panel de gestion"