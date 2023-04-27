# 作者: ZengCheng
# 时间: 2023/4/27

from django.shortcuts import render, redirect
from app01 import models

from app01.utils import Public_Function

""" ++++++++++++++++++++++++++++++++++++++++++ 部门管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 部门列表函数 ------- #
def department_list(request):
    # 查询部门表中的所有数据
    department_data = models.Department.objects.all()
    # 传入部门数据并渲染页面
    return render(request, "department_list.html", {"department_data": department_data})


# ------- 新增部门函数 ------- #
def department_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 跳转到部门新增页面
        return render(request, "department_add.html")

    # 获取POST请求协议的数据
    department_name = request.POST.get('department_name')
    if department_name == '':
        # 跳转到部门新增页面
        return render(request, "department_add.html", {"message": "请输入部门名称！"})
    # 在表中写入数据
    models.Department.objects.create(department_name=department_name, create_time=Public_Function.format_time())
    # 重定向到部门列表页面
    return redirect('/department/list')


# ------- 部门删除函数 ------- #
def department_delete(request, department_id):
    # 删除部门表指定部门id的数据
    models.Department.objects.filter(id=department_id).delete()
    # 重定向到部门列表页面
    return redirect('/department/list')


# ------- 部门修改函数 ------- #
def department_edit(request, department_id):
    department_data = models.Department.objects.filter(id=department_id).first()
    # 如果请求协议为GET
    if request.method == 'GET':
        return render(request, 'department_edit.html', {"department_data": department_data})

    # 获取POST请求协议的数据
    new_department_name = request.POST.get('department_name')
    if new_department_name == '':
        # 跳转到部门修改页面
        return render(request, 'department_edit.html', {"department_data": department_data})
    # 在表中修改数据
    models.Department.objects.filter(id=department_id).update(department_name=new_department_name,
                                                              update_time=Public_Function.format_time())
    # 重定向到部门列表页面
    return redirect('/department/list')