from django import template
import costs.views as views

register = template.Library()


@register.inclusion_tag('costs/include/menu.html')
def show_menu():
    ref = [
        {'title': 'Wallet', 'url_name': 'wallet'},
        {'title': 'Costs', 'url_name': 'costs'},
        {'title': 'Buys', 'url_name': 'buys'},
    ]
    return {'ref': ref}