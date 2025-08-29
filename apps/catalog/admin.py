from django.contrib import admin
from .models import Category, Product, Manufacturer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "prescription_required")
    list_filter = ("category", "prescription_required")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
