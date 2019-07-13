from django import template
import re

register = template.Library()


from django.conf import settings


@register.inclusion_tag('menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)

    # url = request.path_info
    #
    # for item in menu_list:
    #     if re.match(item['url'],url):
    #         item['class'] = 'active'



    return {'menu_list':menu_dict.values()}

