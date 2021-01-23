from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Product

def index(request):
    obj_list = Product.objects.filter(status='in_stock')
    paginator = Paginator(obj_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(1)
    except PageNotAnInteger:
        products = paginator.page(paginator.num_pages)
    
    context = {'products':products}

    return render(request, 'fcz/index.html', context)


def product_detail(request, day, month, year, product):
    product = get_object_or_404(Product, upload__day=day,
                                         upload__month=month,
                                         upload__year=year,
                                         slug=product)
    features = product.features.all()

    context = {'product':product, "features":features}
    return render(request, 'fcz/product_detail.html', context)