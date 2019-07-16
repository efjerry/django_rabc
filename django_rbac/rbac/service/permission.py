from django.conf import settings


def init_permission(request,obj):
    permission_query = obj.roles.all().filter(permissions__url__isnull=False).values('permissions__title',
                                                                                     'permissions__url',
                                                                                     'permissions__name',
                                                                                     'permissions__menu__name',
                                                                                     'permissions__menu__icon',
                                                                                     'permissions__menu__id',
                                                                                     'permissions__menu__weight',
                                                                                     'permissions__id',
                                                                                     'permissions__parent_id',
                                                                                     'permissions__parent__name',   #父权限的别名
                                                                                     ).distinct()

    # 保存权限信息
    permission_dict = {}

    # 保存菜单信息
    menu_dict = {}

    for item in permission_query:
        # 将权限信息放入permission_list
        permission_dict[item['permissions__name']] = {'url': item['permissions__url'],
                                'id':item['permissions__id'],
                                'pname':item['permissions__parent__name'],
                                'pid':item['permissions__parent_id'],
                                'title':item['permissions__title']}

        # 放入菜单信息
        menu_id = item.get('permissions__menu__id')
        # print(menu_id)

        if not menu_id:
            continue

        if menu_id not in menu_dict:

            menu_dict[menu_id] = {'name': item['permissions__menu__name'],
                                  'icon': item['permissions__menu__icon'],
                                  'weight':item['permissions__menu__weight'],
                                  'children': [{'title': item['permissions__title'],
                                                'url': item['permissions__url'],
                                                'id':item['permissions__id']},
                                               ]
                                  }
        else:
            menu_dict[menu_id]['children'].append(
                {'title': item['permissions__title'], 'url': item['permissions__url'],'id':item['permissions__id']})


        # print(menu_dict)

    # 权限保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict

    # 菜单信息保存到session中
    request.session[settings.MENU_SESSION_KEY] = menu_dict