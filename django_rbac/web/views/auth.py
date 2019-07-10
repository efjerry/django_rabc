from django.shortcuts import render, redirect, reverse
from rbac import models


def login(request):

    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(name=user, pwd=pwd).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

        # 保存权限信息
        qr = obj.roles.all().values('permissions__title', 'permissions__title').distinct()
        for i in qr:
            print(i)
    return render(request, 'login.html')