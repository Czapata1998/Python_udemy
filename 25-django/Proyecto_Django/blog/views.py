from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
# Create your views here.
def articles(request):
    
    
    articles = Article.objects.all()
    
    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles' : articles
    })
    
def category(request, category_id):
    # Intentamos obtener la categoría con el ID proporcionado
    category = get_object_or_404(Category, id=category_id)
    
    # Obtener los artículos asociados a esta categoría
    articles = category.article_set.all()  # Asumiendo que la relación se llama 'article_set'
    
    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles,
    })