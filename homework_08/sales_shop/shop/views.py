from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Category
from .models import Product


# def shop_index(request: HttpRequest) -> HttpResponse:
#     products = (
#         Product
#         .objects
#         .filter(~Q(status=Product.Status.ARCHIVED))
#         .order_by("id")
#         .select_related("category")
#         .all()
#     )
#     return render(
#         request=request,
#         template_name="shop/index.html",
#         context={
#             "products": products,
#         },
#     )

class ProductsList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"
    paginate_by = 4

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(name__startswitch='B')
    #     return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = "Super Shop"
        return context


class ProductsCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = "/"

class ShowProducts(DetailView):
    model = Product
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = "{{ product.name }}"
        return context
# def categories_with_products_three(request: HttpRequest) -> HttpResponse:
#     categories = Category.objects.order_by("id").prefetch_related("products").all()
#
#     return render(
#         request=request,
#         template_name="shop/categories-with-products-three.html",
#         context={
#             "categories": categories
#         }
#     )