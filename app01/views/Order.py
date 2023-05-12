# 作者: ZengCheng
# 时间: 2023/5/12
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.utils.ModelForm import OrderModerForm


# ------- 订单列表函数 ------- #
def order_list(request):
    form = OrderModerForm()
    return render(request, 'order_list.html', {"form": form})


# ------- 订单新增函数 ------- #
@csrf_exempt
def order_add(request):
    """ 新增订单（ajax请求） """
    form = OrderModerForm(data=request.POST)
    if form.is_valid():
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
