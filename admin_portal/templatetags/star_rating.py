from django import template

register = template.Library()

@register.filter
def stars(value):
    value = int(value)
    return "★" * value + "☆" * (5 - value)