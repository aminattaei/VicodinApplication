from django.contrib import admin
from django import forms
from .models import (
    User, Address, Category, Product, Inventory,
    Order, OrderItem, Payment, Review,
    Cart, CartItem, AuditLog,ProductImage
)

# ===================== User Admin =====================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# ===================== Address Admin =====================
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'zip_code', 'country')
    search_fields = ('user__username', 'street', 'city', 'country')

# ===================== Category Admin =====================

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    parent = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False  
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name', 'parent')
    search_fields = ('name',)


# ===================== Product Admin =====================

 
class ProductImageInline(admin.TabularInline):  # ی
    model = ProductImage
    extra = 1  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_new', 'is_off')
    list_filter = ('category', 'is_new', 'is_off')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]  


# ===================== Inventory Admin =====================
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'change_type', 'quantity', 'created_at')
    list_filter = ('change_type',)
    search_fields = ('product__name', 'note')

# ===================== Order Admin =====================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username',)

# ===================== OrderItem Admin =====================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')
    search_fields = ('product__name', 'order__id')

# ===================== Payment Admin =====================
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'amount', 'status', 'transaction_id')
    list_filter = ('status', 'payment_method')
    search_fields = ('order__id', 'transaction_id')

# ===================== Review Admin =====================
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'comment')

# ===================== Cart Admin =====================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('product__name',)

# ===================== AuditLog Admin =====================
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'table_name', 'record_id', 'created_at')
    search_fields = ('user__username', 'action', 'table_name')
