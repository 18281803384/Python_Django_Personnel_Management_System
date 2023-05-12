# 作者: ZengCheng
# 时间: 2023/5/9
import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.Bootstrap import Bootstrap_ModelForm
from app01.utils.Paging_Module import Paging_Module
from app01.utils.Public_Function import format_time


class TaskManagerModelForm(Bootstrap_ModelForm):
    class Meta:
        model = models.TaskManager
        fields = ['level','task_title','task_details','task_head']
        widgets = {
            "task_details": forms.TextInput
        }


@csrf_exempt
def task_list(request):
    form = TaskManagerModelForm()

    # 根据字典条件获取表中的数据，并以order_by进行排序，当字典为空时查询所有数据
    task_data = models.TaskManager.objects.all().order_by('id')

    # ------ 分页功能 start
    page_object = Paging_Module(request, task_data)
    # ------ 分页功能 end

    context = {
        "form": form,
        "pretty_data": page_object.page_queryset,
        "page_li_list_string": page_object.show_html()
    }

    return render(request,'task_mg.html',context)


@csrf_exempt
def task_ajax_add(request):
    # 如果请求协议为POST，则获取表单数据
    form = TaskManagerModelForm(data=request.POST)
    # 用户提交的数据进行校验
    if form.is_valid():
        form.instance.create_time = format_time()
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict))

