from django.conf import settings


def init_permission(request,obj):
    permission_query = obj.roles.all().filter(permissions__url__isnull=False).values('permissions__title',
                                                                                     'permissions__url',
                                                                                     'permissions__menu__name',
                                                                                     'permissions__menu__icon',
                                                                                     'permissions__menu__id',
                                                                                     ).distinct()

    # 保存权限信息
    permission_list = []

    # 保存菜单信息
    menu_dict = {}

    for item in permission_query:
        # 将权限信息放入permission_list
        permission_list.append({'url': item['permissions__url']})

        # 放入菜单信息
        menu_id = item.get('permissions__menu__id')

        if not menu_id:
            continue

        if menu_id not in menu_dict:
            menu_dict[menu_id] = {'name': item['permissions__menu__name'], 'icon': item['permissions__menu__icon'],
                                  'children': [{'title': item['permissions__title'], 'url': item['permissions__url']}]}
        else:
            menu_dict[menu_id]['children'].append(
                {'title': item['permissions__title'], 'url': item['permissions__url']})




    # 权限保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list

    # 菜单信息保存到session中
    request.session[settings.MENU_SESSION_KEY] = menu_dict