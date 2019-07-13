from django.shortcuts import render, redirect, reverse
from rbac import models
from django.conf import settings
from rbac.service.permission import init_permission


def login(request):

    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(name=user, pwd=pwd).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})


        init_permission(request,obj)



        return redirect(reverse('customer_list'))
    return render(request, 'login.html')