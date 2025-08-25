from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',views.ProductViewSet,basename="product-view-set")

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('api/',include(router.urls))
]
