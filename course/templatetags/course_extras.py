from django import template

register = template.Library()

@register.filter
def rep(value):
    return value.replace("_"," ")