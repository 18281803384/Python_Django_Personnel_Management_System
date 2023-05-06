# 作者: ZengCheng
# 时间: 2023/4/27
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.Paging_Module import Paging_Module
from app01.utils.ModelForm import AdminAddModelForm,AdminEditModelForm,AdminPsResetModelForm
from app01.utils import Public_Function


def admin_list(request):
    admin_data = models.Admin.objects.all().order_by('create_time')

    # ------ 分页功能 start
    page_object = Paging_Module(request, admin_data)
    # ------ 分页功能 end

    context = {
        "admin_data": page_object.page_queryset,
        "page_li_list_string": page_object.show_html()
    }

    # 传入数据并渲染页面显示
    return render(request, 'admin_list.html', context)


def admin_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = AdminAddModelForm()
        # 传入数据并渲染页面
        return render(request, 'admin_add.html', {"form": form})

    # 如果请求协议为POST，则获取表单数据
    form = AdminAddModelForm(data=request.POST)
    # 用户提交的数据进行校验
    if form.is_valid():
        form.instance.create_time = Public_Function.format_time()
        # 验证成功则保存数据到mysql
        form.save()
        return redirect('/admin/list')
    # 验证不成功则范围页面给出提示
    return render(request, 'admin_add.html', {"form": form})


def admin_edit(request, admin_id):
    # 查询该id的数据
    row_admin = models.Admin.objects.filter(id=admin_id).first()
    # 验证是否存在该数据
    if not row_admin:
        # 不存在则跳转错误页面提示
        return render(request, 'error.html', {"message": '数据错误！'})

    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = AdminEditModelForm(instance=row_admin)
        # 传入数据并渲染页面
        return render(request, 'admin_edit.html', {"form": form})

    # 如果请求协议为POST，则获取表单数据
    form = AdminEditModelForm(data=request.POST, instance=row_admin)
    # 用户提交的数据进行校验
    if form.is_valid():
        form.instance.update_time = Public_Function.format_time()
        # 验证成功则保存数据到mysql
        form.save()
        return redirect('/admin/list')
    # 验证不成功则范围页面给出提示
    return render(request, 'admin_edit.html', {"form": form})


def admin_delete(request, admin_id):
    models.Admin.objects.filter(id=admin_id).delete()
    return redirect('/admin/list')


def admin_ps_reset(request, admin_id):
    # 查询该id的数据
    row_admin = models.Admin.objects.filter(id=admin_id).first()
    # 验证是否存在该数据
    if not row_admin:
        # 不存在则跳转错误页面提示
        return render(request, 'error.html', {"message": '数据错误！'})

    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = AdminPsResetModelForm(instance=row_admin)
        # 传入数据并渲染页面
        return render(request, 'admin_ps_reset.html', {'form': form, 'admin_name':row_admin.admin_name})

    # 如果请求协议为POST，则获取表单数据
    form = AdminPsResetModelForm(data=request.POST,instance=row_admin)
    # 用户提交的数据进行校验
    if form.is_valid():
        form.instance.update_time = Public_Function.format_time()
        # 验证成功则保存数据到mysql
        form.save()
        return redirect('/admin/list')
    # 验证不成功则范围页面给出提示
    return render(request, 'admin_ps_reset.html', {'form': form, 'admin_name': row_admin.admin_name})


