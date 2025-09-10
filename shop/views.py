from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.views import generic

from .models import Product,Order,ProductImage
from .serializers import ProductSerializer,OrderSerializer,ProductImageSerializer


# Shop views

def home_page(request):
    return render(request,"Index/index.html",{})


# def product_list(request):
#     products = Product.objects.all()
#     return render(request,"Shop/shop.html",{'products':products})

# def product_detail(request,pk):
#     product = get_object_or_404(Product,id = pk)
#     product_image = product.images.all()
#     context = {'product':product,'product_images':product_image}
#     return render(request,"Shop/product-details.html",context)

# Api Views

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    permission_classes =[IsAuthenticated]
        

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes =[IsAuthenticated]

class ProductImageModelViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes =[IsAuthenticated]

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = "Shop/shop.html"



class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "Shop/product-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orginal_img'] = self.object.images.first()
        context['images'] = self.object.images.all()
        return context
