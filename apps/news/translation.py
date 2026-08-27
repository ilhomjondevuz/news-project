from modeltranslation.translator import TranslationOptions, register
from .models import Newness, Category

@register(Newness)
class NewnessTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )