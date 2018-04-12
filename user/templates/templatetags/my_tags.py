from django import template
register = template.Library()

@register.filter
def multiply(arg1,arg2):
    return sum(d.get('pro_id_id.price') for d in arg)