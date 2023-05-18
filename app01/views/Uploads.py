# 作者: ZengCheng
# 时间: 2023/5/18
from django.http import HttpResponse
from django.shortcuts import render

from app01.utils import Form


# ------- Form 文件上传函数 ------- #
def uploads_list(request):
    if request.method == 'GET':
        form = Form.upload_form()
        return render(request, 'uploads_list.html', {"form": form})

    form = Form.upload_form(data=request.POST, files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse('From 文件上传成功！')
    return render(request, 'uploads_list.html', {"form": form})