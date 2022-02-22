import re
from django import template

register = template.Library()

@register.filter(name='censor')

def censor(value):

    black_list = ['nigger', 'приказ Израиля', 'NFT', '1xbt']

    for word in black_list:
        value = value.replace(word, '***')
    return value
