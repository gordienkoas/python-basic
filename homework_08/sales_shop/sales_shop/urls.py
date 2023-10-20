from django.urls import path, include
#from .views import shop_index, categories_with_products_three
import shop.views as shop
from django.conf import settings

app_name = "sales_shop"

urlpatterns = [
    #path("", shop.index),
    path('', shop.ProductsList.as_view(), name='shop'),
    path('create/', shop.ProductsCreate.as_view(), name='create'),
    path('<int:pk>/', shop.ShowProducts.as_view(), name='detail'),
    #path('send/', main.send_mail),
    #path("categories-as-three/", categories_with_products_three, name="categories_with_products_three"),
]
# if settings.DEBUG:
#     urlpatterns.append(
#     path("__debug__/", include("debug_toolbar.urls")),
#     )