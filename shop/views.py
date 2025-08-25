from django.shortcuts import render

from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

def home_page(request):
    return render(request,"Index/index.html",{})


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    