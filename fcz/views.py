from django.shortcuts import render,\
                    get_object_or_404
from django.core.paginator import Paginator,\
             PageNotAnInteger, EmptyPage
from django.contrib.postgres.search import \
        SearchVector, SearchRank, SearchQuery



from taggit.models import Tag

from .models import Product, Categorie
from .forms import SearchForm

def index(request):
    categs = Categorie.objects.all()
    all_products = Product.in_stock.all()
    products = {}
    #form, results = search(request)
    for categ in categs:
        tag = get_object_or_404(Tag, slug=categ.slug)
        products[categ.title]=all_products.filter(tags__in=[tag])

    context = {'products':products}
    return render(request, 'fcz/index.html', context)

def category(request, categ, sub_categ=None):
    obj_list = Product.objects.filter(status='in_stock')    
    tag = get_object_or_404(Tag, slug=categ)
    obj_list = obj_list.filter(tags__in=[tag])
    
    if sub_categ:
        tag = get_object_or_404(Tag, slug=sub_categ)

        obj_list = obj_list.filter(tags__in=[tag])
    paginator = Paginator(obj_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)
    
    context = {'products':products}

    return render(request, 'fcz/category.html', context)


def product_detail(request, day, month, year, product):
    product = get_object_or_404(Product, upload__day=day,
                                         upload__month=month,
                                         upload__year=year,
                                         slug=product)
    features = product.features.all()

    context = {'product':product, "features":features}
    return render(request, 'fcz/product_detail.html', context)

def search(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('name', 'tags')
            results = Product.in_stock.annotate(
                search = search_vector,
            ).filter(search=query)
            
            
    context = {'form':form, 'products':results}
    return render(request, 'fcz/category.html', context)