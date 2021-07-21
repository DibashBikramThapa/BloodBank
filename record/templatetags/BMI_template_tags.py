"""from django import template
from record.models import height_m, weight_kg

register = template.Library()

@register.filter
def BMIValue(user):
    return height_m/(weight_kg **2)"""
