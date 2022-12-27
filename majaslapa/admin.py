from unicodedata import category
from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin
from.models import Category, ProductType, ProductSpecification, Product, ProductSpecificationValue, ProductImage
from modeltranslation.admin import TranslationAdmin

# Register your models here.
# admin.site.register(Category)
# admin.site.register(ProductType)
# admin.site.register(ProductSpecification)e
# admin.site.register(Product)
# admin.site.register(ProductSpecificationValue)
# admin.site.register(ProductImage)



admin.site.register(Category, MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline, ProductImageInline
    ]
