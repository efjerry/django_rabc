from django.shortcuts import render, redirect, reverse
from rbac import models
from django.conf import settings


def login(request):

    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(name=user, pwd=pwd).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

        # 保存权限信息
        permission_list = obj.roles.all().filter(permissions__url__isnull=False).values('permissions__title',
                                                                                        'permissions__url').distinct()

        request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)

        # print(list(permission_list))


        return redirect(reverse('customer_list'))
    return render(request, 'login.html')