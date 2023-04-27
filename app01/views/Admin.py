# 作者: ZengCheng
# 时间: 2023/4/27
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.Paging_Module import Paging_Module
from app01.utils.ModelForm import AdminModelForm
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
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'admin_add.html', {"form": form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.instance.create_time = Public_Function.format_time()
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_add.html', {"form": form})
