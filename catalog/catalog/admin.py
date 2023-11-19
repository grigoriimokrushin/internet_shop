from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Category)
class CategAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProdAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'category',)
