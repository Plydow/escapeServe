from django import template

register = template.Library()

@register.filter
def get_type(value, target):
    return type(value).__name__ == target
