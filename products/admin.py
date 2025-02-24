from django.contrib import admin
from .models import Product,ProductImage,Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'quantity', 'owner', 'category', 'is_new', 'address')  # Ensure 'stock' is a valid field or method on Product model

    # list_filter = ('category', 'stock')
    # autocomplete_fields = ['category']
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    
    # autocomplete_fields = ['product']

@admin.register(Category)  # Correct: use the plural form of the model name (Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')  # Correct: use a tuple or list

    # autocomplete_fields = ['products']