# 作者: ZengCheng
# 时间: 2023/5/8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from io import BytesIO

from app01.utils.Form import LoginForm
from app01 import models
from app01.utils.Public_Function import check_code


# 用户登录
def login(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = LoginForm()
        # 传入数据并渲染页面
        return render(request, 'login.html',{"form":form})
    # 如果请求协议为POST，则获取表单数据
    form = LoginForm(data=request.POST)
    # 用户提交的数据进行校验
    if form.is_valid():
        # 查询用户输入数据在数据库是否存在，不存在则为None
        data = models.Admin.objects.filter(**form.cleaned_data).first()
        # 如果不存在则
        if not data:
            # 添加错误信息
            form.add_error("password","账号或密码错误!")
            # 数据不存在则范围页面给出提示
            return render(request, 'login.html', {"form": form})
        request.session["info"] = {'id':data.id, 'account':data.account, 'admin_name':data.admin_name}
        # 如果存在则返回到指定页面
        return redirect('/admin/list')
    # 验证不成功则范围页面给出提示
    return render(request, 'login.html', {"form": form})


# 获取图片验证码
def image_code(request):
    # 调用方法获取验证码图片和验证码文字
    img,code_string = check_code()
    # 写入内存(Python3)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


# 用户退出登录
def logout(request):
    # 清除session信息
    request.session.clear()
    # 返回到登录页面
    return redirect('/login')