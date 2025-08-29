from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, slug=None):
    category = None
    categories = Category.objects.all().order_by('name')
    products = Product.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    q = request.GET.get("q")
    if q:
        products = products.filter(name__icontains=q)
    return render(request, 'catalog/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'catalog/product_detail.html', {'product': product})
