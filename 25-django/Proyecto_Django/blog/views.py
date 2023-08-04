from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def articles(request):
    
    #Sacar articulos
    articles = Article.objects.all()
    
    #Paginar articulos
    paginator = Paginator(articles, 2)
    
    
    #Recoger numero de pagina
    
    page = request.GET.get('page')
    
    page_articles = paginator.get_page(page)
    
    
    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles' : page_articles
    })

@login_required(login_url="login")  
def category(request, category_id):
    # Intentamos obtener la categoría con el ID proporcionado
    category = get_object_or_404(Category, id=category_id)
    
    # Obtener los artículos asociados a esta categoría
    #articles = Article.objects.filter(categories=category) # Asumiendo que la relación se llama 'article_set'
    
    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles,
    })

@login_required(login_url="login")
def article(request, article_id): 
    
    article = get_object_or_404(Article, id=article_id)
    
    return render(request, 'articles/detail.html', {
       'article' : article
        
    })