from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import manage_profile,add_product,view_orders,update_product,delete_product,view_products,product_list,farmer_dashboard

urlpatterns = [
    path('',farmer_dashboard,name='farmer_dashboard'),
    path('products/',product_list, name='product_list'),
    path('profile/', manage_profile, name='manage_profile'),
    path('products/add/', add_product, name='add_product'),
    path('products/',view_products, name='view_products'),
    path('products/<int:product_id>/update/',update_product, name='update_product'),
    path('products/<int:product_id>/delete/',delete_product, name='delete_product'),
    path('orders/',view_orders, name='view_orders'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)