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
        # 获取用户输入的验证码字符串
        text_image_code = form.cleaned_data.pop('image_code')
        # 获取正确的图片验证码字符串
        code = request.session.get('image_code','')
        # 如果输入的验证码信息与图片的不一致则
        if text_image_code.upper() != code.upper():
            form.add_error("image_code","验证码错误!")
            # 数据不存在则范围页面给出提示
            return render(request, 'login.html', {"form": form})

        # 查询用户输入数据在数据库是否存在，不存在则为None
        data = models.Admin.objects.filter(**form.cleaned_data).first()
        # 如果不存在则
        if not data:
            # 添加错误信息
            form.add_error("password","账号或密码错误!")
            # 数据不存在则范围页面给出提示
            return render(request, 'login.html', {"form": form})
        # 用户名密码验证码正确的话，则生成session
        request.session["info"] = {'id':data.id, 'account':data.account, 'admin_name':data.admin_name}
        # 设置session超时 7天免登陆
        request.session.set_expiry(60 * 60 * 12 * 7)
        # 如果存在则返回到指定页面
        return redirect('/admin/list')
    # 验证不成功则范围页面给出提示
    return render(request, 'login.html', {"form": form})


# 获取图片验证码
def image_code(request):
    # 调用pillow函数，生成图片
    img,code_string = check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给session设置60s后超时
    request.session.set_expiry(60)

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