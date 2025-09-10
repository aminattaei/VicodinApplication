from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Products',views.ProductViewSet,basename="product-view-set")
router.register('Orders',views.OrderViewSet,basename='orders-api')
router.register('ProductImage',views.ProductImageModelViewSet,basename='product-image-api')

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('api/',include(router.urls)),
    path('products/',views.ProductListView.as_view(),name='shop_page'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name='Product_detail')
]
