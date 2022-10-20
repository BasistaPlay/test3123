from modeltranslation.translator import register, TranslationOptions
from .models import *

# @register(ProductSpecificationValue)
# class CategoryTranslationOption(TranslationOptions):
#     fields = ("value")

@register(Product)
class CategoryTranslationOption(TranslationOptions):
    fields = ('category', 'title', 'desciption')

# @register(ProductSpecification)
# class CategoryTranslationOption(TranslationOptions):
#     fields = ('name')