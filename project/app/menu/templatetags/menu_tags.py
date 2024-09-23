
from django import template

from django.urls import resolve

from menu.models import MenuItem



register = template.Library()

@register.simple_tag(takes_context=True)


def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    try:
        matched_item = MenuItem.objects.get(url=current_url)
        active_item = matched_item
    except MenuItem.DoesNotExist:
        active_item = None


    menu_items = MenuItem.objects.filter(menu_name=menu_name)


    def get_nested_items(item):
        children = item.children.all()
        return {
            'item': item,
            'children': [get_nested_items(child)for child in children]
        }
    
    menu_tree = [get_nested_items(item) for item in menu_items if item.parent is None]


    return {
        'menu_tree': menu_tree,
        'active_item': active_item,
    }


