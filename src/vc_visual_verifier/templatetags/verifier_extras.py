from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(value, arg):
    """Removes all values of arg from the given string"""
    separator = arg or " "
    return value.split(separator)
