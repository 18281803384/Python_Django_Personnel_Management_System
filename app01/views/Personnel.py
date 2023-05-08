# 作者: ZengCheng
# 时间: 2023/4/27
from django.shortcuts import render, redirect
from app01 import models

from app01.utils.ModelForm import PersonnelAddModelForm,PersonnelEditModelForm
from app01.utils import Public_Function

""" ++++++++++++++++++++++++++++++++++++++++++ 员工管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 员工列表函数 ------- #
def personnel_list(request):
    # 查询员工表中的所有数据
    personnel_data = models.Personnel.objects.all()
    # 传入员工数据并渲染页面
    return render(request, "personnel_list.html", {"personnel_data": personnel_data})


# ------- 员工添加函数 ------- #
def personnel_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        data = {
            "department_info": models.Department.objects.all(),
            "gender_choices": models.Personnel.gender_choices
        }
        # 传入数据并渲染页面
        return render(request, 'personnel_add.html', data)

    # 获取POST请求协议的数据
    personnel_name = request.POST.get('personnel_name')
    account = request.POST.get('account')
    password = request.POST.get('password')
    department = request.POST.get('department')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    salary = request.POST.get('salary')

    # 在表中写入数据
    models.Personnel.objects.create(personnel_name=personnel_name, account=account, password=password, department_id=department, gender=gender, age=age,
                                    salary=salary, create_time=Public_Function.format_time())
    # 重定向到部门列表页面
    return redirect('/personnel/list')


# ------- 员工添加函数 基于ModelForm ------- #
def personnel_model_form_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = PersonnelAddModelForm()
        # 传入数据并渲染页面
        return render(request, 'personnel_model_form_add.html', {"form": form})

    # 用户提交的数据进行校验
    form = PersonnelAddModelForm(data=request.POST)
    # 如果数据合法
    if form.is_valid():
        form.instance.create_time = Public_Function.format_time()
        # 保存数据到表中
        form.save()
        # 重定向到部门列表页面
        return redirect('/personnel/list')
    # 数据校验失败，则继续跳转到页面显示错误信息
    return render(request, 'personnel_model_form_add.html', {"form": form})


# ------- 员工修改函数 ------- #
def personnel_edit(request, personnel_id):
    row_personnel = models.Personnel.objects.filter(id=personnel_id).first()
    if not row_personnel:
        return render(request, 'error.html', {"message": '数据错误！'})

    if request.method == 'GET':
        # 实例化类
        form = PersonnelEditModelForm(instance=row_personnel)
        # 传入数据并渲染页面
        return render(request, 'personnel_edit.html', {"form": form})

    # instance指定数据
    form = PersonnelEditModelForm(data=request.POST, instance=row_personnel)
    if form.is_valid():
        # 额外保存另外的值
        form.instance.update_time = Public_Function.format_time()
        # 保存数据到表中
        form.save()
        # 重定向到部门列表页面
        return redirect('/personnel/list')

    # 数据校验失败，则继续跳转到页面显示错误信息
    return render(request, 'personnel_edit.html', {"form": form})


# ------- 员工删除函数 ------- #
def personnel_delete(request, personnel_id):
    # 删除员工表指定员工id的数据
    models.Personnel.objects.filter(id=personnel_id).delete()
    # 重定向到部门列表页面
    return redirect('/personnel/list')
