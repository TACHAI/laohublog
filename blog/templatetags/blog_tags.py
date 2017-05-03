from django import template
from django.db.models.aggregates import Count

from ..models import Aritcle, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Aritcle.objects.all()[:num]


@register.simple_tag
def archives():
    return Aritcle.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))
