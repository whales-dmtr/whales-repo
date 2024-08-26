from django import template
import costs.views as views

register = template.Library()


@register.simple_tag(name='get_all_catgs')
def get_categories():
    return views.data_categories

@register.inclusion_tag('costs/include/menu.html')
def show_menu():
    ref = [
        {'title': 'Wallet', 'url_name': 'wallet'},
        {'title': 'Costs', 'url_name': 'costs'},
    ]
    return {'ref': ref}