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
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        print(permission_dict)

        #校验是否登录
        if not permission_dict:
            return redirect(reverse('login'))

        request.current_menu_id = None

        #保存路径导航的信息
        request.breadcrumb_list = [{'title':'首页','url':'/index/'}]

        # 设置需要登录，不需要权限的页面
        for i in settings.NONEED_PERMISSION_LIST:
            if re.match(i,url):
                return



        # 权限校验
        for item in permission_dict.values():

            # 找到当前访问的url对应的权限
            if re.match("^{}$".format(item['url']), url):

                pid = item['pid']
                id = item['id']

                if pid:
                    request.current_menu_id = pid
                    request.breadcrumb_list.append({'title':permission_dict[str(pid)]['title'],'url':permission_dict[str(pid)]['url']})
                    request.breadcrumb_list.append({'title': item['title'], 'url': item['url']})
                else:
                    request.current_menu_id = id
                    request.breadcrumb_list.append({'title':item['title'],'url':item['url']})

                return


        return HttpResponse('没有访问权限')