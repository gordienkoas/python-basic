from django.urls import path
from .views import shop_index, categories_with_products_three

app_name = "shop"

urlpatterns = [
    path("", shop_index, name="index"),
   # path('send/', main.send_mail),
    path("categories-as-three/", categories_with_products_three, name="categories_with_products_three"),
]
