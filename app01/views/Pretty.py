# 作者: ZengCheng
# 时间: 2023/4/27
from django.shortcuts import render, redirect
from app01 import models

from app01.utils.ModelForm import PrettyAddModelForm, PrettyEditModelForm
from app01.utils import Public_Function
from app01.utils.Paging_Module import Paging_Module

""" ++++++++++++++++++++++++++++++++++++++++++ 靓号管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 靓号列表函数 ------- #
def pretty_list(request):
    # ------ 查询功能 start
    data_dict = {}
    # 获取get请求传来的数据
    search_data = request.GET.get('search', '')
    # 如果有数据，则添加至字典中
    if search_data:
        data_dict["mobile__contains"] = search_data
    # ------ 查询功能 end

    # 根据字典条件获取表中的数据，并以order_by进行排序，当字典为空时查询所有数据
    pretty_data = models.Pretty.objects.filter(**data_dict).order_by('id')

    # ------ 分页功能 start
    page_object = Paging_Module(request, pretty_data)
    # ------ 分页功能 end

    context = {
        "pretty_data": page_object.page_queryset,
        "search_data": search_data,
        "page_li_list_string": page_object.show_html()
    }

    # 传入数据并渲染页面显示
    return render(request, 'pretty_list.html', context)


# ------- 靓号添加函数 ------- #
def pretty_add(request):
    if request.method == 'GET':
        form = PrettyAddModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyAddModelForm(data=request.POST)
    if form.is_valid():
        form.instance.create_time = Public_Function.format_time()
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_add.html', {"form": form})


# ------- 靓号修改函数 ------- #
def pretty_edit(request, pretty_id):
    row_pretty = models.Pretty.objects.filter(id=pretty_id).first()
    if request.method == 'GET':
        form = PrettyEditModelForm(instance=row_pretty)
        return render(request, 'pretty_edit.html', {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_pretty)
    if form.is_valid():
        form.instance.update_time = Public_Function.format_time()
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_edit.html', {"form": form})


# ------- 靓号删除函数 ------- #
def pretty_delete(request, pretty_id):
    models.Pretty.objects.filter(id=pretty_id).delete()
    return redirect('/pretty/list')
