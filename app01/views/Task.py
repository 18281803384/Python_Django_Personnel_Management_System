# 作者: ZengCheng
# 时间: 2023/5/9
import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.Bootstrap import Bootstrap_ModelForm
from app01.utils.Public_Function import format_time


class TaskManagerModelForm(Bootstrap_ModelForm):
    class Meta:
        model = models.TaskManager
        fields = ['level','task_title','task_details','task_head']
        widgets = {
            "task_details": forms.TextInput
        }


@csrf_exempt
def task_mg(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        form = TaskManagerModelForm()
        return render(request,'task_mg.html',{"form":form})
    # 如果请求协议为POST，则获取表单数据
    form = TaskManagerModelForm(data=request.POST)
    # 用户提交的数据进行校验
    if form.is_valid():
        form.instance.create_time = format_time()
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "error":form.errors}
    return HttpResponse(json.dumps(data_dict))

