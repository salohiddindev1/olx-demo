from django.db import models

class BASE(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BASE):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)
    address = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
    

class Category(BASE):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['name']
    
class ProductImage(BASE):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images')

    class Meta:
        verbose_name_plural = 'Product Images'
        verbose_name = 'Product Image'

    def __str__(self):
        return f'Image of {self.image.name}'
