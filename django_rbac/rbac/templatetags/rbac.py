from django import template
import re
from collections import OrderedDict

register = template.Library()


from django.conf import settings


@register.inclusion_tag('menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    print(menu_dict)

    order_dic = OrderedDict()

    for key in sorted(menu_dict, key=lambda i: menu_dict[i]['weight'], reverse=True):

        order_dic[key] = item = menu_dict[key]

        item['class'] = 'hide'

        for i in item['children']:

            # if re.match('^{}$'.format(i['url']),request.path_info):
            if i['id'] == request.current_menu_id:
                i['class'] = 'active'
                item['class'] = ''
                break



    return {'menu_list':order_dic.values()}


@register.inclusion_tag('breadcrumb.html')
def breadcrumb(request):
    return {'breadcrumb_list': request.breadcrumb_list}


@register.filter()
def has_permission(request,name):
    if name in request.session.get(settings.PERMISSION_SESSION_KEY):
        return True