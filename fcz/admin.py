from django.contrib import admin

from .models import Product, Feature

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'status')
    list_filter = ('brand', 'status', 'upload', 'update')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('ft_name', 'ft_value')
    list_filter = ('product',)