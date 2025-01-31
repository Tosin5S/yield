from django import template

register = template.Library()

@register.filter
def getattr_custom(obj, attr):
    """Custom template filter to get attribute dynamically"""
    return getattr(obj, attr, "")

