from modeltranslation.translator import translator, TranslationOptions
from product.models import Category


class CategoryTranslationsOptions(TranslationOptions):
    fields = ('title',)




translator.register(Category, CategoryTranslationsOptions)