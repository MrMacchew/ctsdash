from django import template
import inflection

register = template.Library()

@register.filter(name='inflect')
def inflect(value):
    return inflection.ordinalize(value[0])


