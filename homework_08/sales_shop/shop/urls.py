from django.template.defaulttags import url
from django.urls import path, include
#from .views import shop_index, categories_with_products_three
import shop.views as shop
from shop import admin

app_name = "shop"

urlpatterns = [
    #path("", shop.index),
    #path('', shop.ProductsList.as_view()),
    path('', include('shop.urls', namespace='products')),
    path('auth/', include('myauth.urls', namespace='myauth')),
    path('admin/', admin.site.urls),
    #path('create/', shop.ProductsList.as_view()),
    #path('send/', main.send_mail),
    #path("categories-as-three/", categories_with_products_three, name="categories_with_products_three"),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]