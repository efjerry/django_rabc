from django.conf import settings


def init_permission(request,obj):
    permission_query = obj.roles.all().filter(permissions__url__isnull=False).values('permissions__title',
                                                                                     'permissions__url',
                                                                                     'permissions__is_menu',
                                                                                     'permissions__icon').distinct()

    # 保存权限信息
    permission_list = []

    # 保存菜单信息
    menu_list = []

    for item in permission_query:
        print(item)
        permission_list.append({'url': item['permissions__url']})
        if item['permissions__is_menu']:
            menu_list.append({'icon': item['permissions__icon'], 'title': item['permissions__title'],
                              'url': item['permissions__url']})

    print(menu_list)

    # 权限保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list

    # 菜单信息保存到session中
    request.session[settings.MENU_SESSION_KEY] = menu_list