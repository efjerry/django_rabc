from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse, redirect, reverse
import re


class RbacMiddleware(MiddlewareMixin):

    def process_request(self,request):

        # 获取当前访问的url
        url = request.path_info
        # print(url)

        # 设置白名单
        for i in settings.WHITE_LIST:
            if re.match(i,url):
                return

        # 获取权限信息
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        # print(permission_list)

        if not permission_list:
            return redirect(reverse('login'))

        # 权限校验
        for item in permission_list:

            # 找到当前访问的url对应的权限
            if re.match("^{}$".format(item['url']), url):

                pid = item['pid']
                id = item['id']

                if pid:
                    request.current_menu_id = pid
                else:
                    request.current_menu_id = id

                return


        return HttpResponse('没有访问权限')