from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Category
from .models import Product
def shop_index(request: HttpRequest) -> HttpResponse:
    products = (
        Product
        .objects
        .filter(~Q(status=Product.Status.ARCHIVED))
        .order_by("id")
        .select_related("category")
        .all()
    )
    return render(
        request=request,
        template_name="shop/index.html",
        context={
            "products": products,
        },
    )

def categories_with_products_three(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.order_by("id").prefetch_related("products").all()

    return render(
        request=request,
        template_name="shop/categories-with-products-three.html",
        context={
            "categories": categories
        }
    )