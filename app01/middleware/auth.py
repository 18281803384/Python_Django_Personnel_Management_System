# 作者: ZengCheng
# 时间: 2023/5/8
# 备注: 建立Django中间件
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        if request.path_info == '/':
            return redirect('/login/')

        # 如果用户访问的是登录页面则不需要判断session信息
        if request.path_info in ['/login/', '/image/code/']:
            return

        # 读取当前访问用户的session信息，如果能读取到，说明已经登录，就可以继续向前走
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 如果读取不到session用户信息，则重定向到login页面
        return redirect('/login/')
