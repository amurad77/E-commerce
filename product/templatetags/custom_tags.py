from django.template import Library
from django.utils import safestring
from product.models import OptionsAttributes

register = Library()

@register.simple_tag
def get_attributes(product, option):
    return product.attributess.filter(optionsattribute__option__title__iexact=option)

@register.simple_tag
def get_attributes2(option):
    return OptionsAttributes.objects.filter(option__title__iexact=option)

@register.simple_tag
def rewiev_count_range(count):
    s = ''
    for i in range(5):
        if i < count:
            s += '<i class=" fa fa-star " style="color:#ffa200"></i>'
        else:
            s += '<i class=" fa fa-star" style="color:#dddddd"></i>'
    return safestring.mark_safe(s)