# 作者: ZengCheng
# 时间: 2023/5/9
from django.shortcuts import render


def ajax(request):
    return render(request,'task_mg.html')