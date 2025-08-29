from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    prescription_required = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, help_text='Maximum Retail Price')
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self): return self.name
