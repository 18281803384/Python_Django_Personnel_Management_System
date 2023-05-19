# 作者: ZengCheng
# 时间: 2023/5/18
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils import Form, ModelForm
from app01.utils import Public_Function
from app01.utils.Paging_Module import Paging_Module


# ------- Form 文件上传函数 ------- #
def form_uploads_list(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化Form类
        form = Form.upload_form()
        # 跳转页面并数据渲染
        return render(request, 'form_uploads_list.html', {"form": form})

    # 获取请求协议为POST提交的表单数据
    form = Form.upload_form(data=request.POST, files=request.FILES)
    # 如果校验表单数据成功
    if form.is_valid():
        # 获取表单上传的文件对象
        img_object = form.cleaned_data.get('head_sculpture')
        """os.path.join() 路径合并函数，把所有参数合并成一个路径字符串"""
        # 文件存放的位置路径
        media_path = os.path.join('media/', img_object.name)
        # 以二进制写入的方式打开该文件
        with open(media_path, 'wb') as f:
            # 循环读取文件对象数据
            for chunk in img_object.chunks():
                # 每读取一次就写入到本地文件中
                f.write(chunk)

        models.Form_Uploads.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            head_sculpture=media_path,
            create_time=Public_Function.format_time()
        )
        return HttpResponse('From 文件上传成功！')
    # 校验表单数据失败，则跳转页面并错误数据渲染
    return render(request, 'form_uploads_list.html', {"form": form})


# ------- ModelForm 文件上传函数 ------- #
def modelform_uploads_list(request):
    if request.method == 'GET':
        query_all_data = models.ModelForm_Uploads.objects.all().order_by('-id')

        # ------ 分页功能 start
        page_object = Paging_Module(request, query_all_data)
        # ------ 分页功能 end

        # 实例化ModelForm类
        form = ModelForm.upload_modelform()

        context = {
            "form": form,
            "query_data": page_object.page_queryset,
            "page_li_list_string": page_object.show_html()
        }
        # 跳转页面并数据渲染
        return render(request, 'modelform_uploads_list.html', context)

    form = ModelForm.upload_modelform(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/modelform/uploads/list')

    # 校验表单数据失败，则跳转页面并错误数据渲染
    return render(request, 'modelform_uploads_list.html', {"form": form})
