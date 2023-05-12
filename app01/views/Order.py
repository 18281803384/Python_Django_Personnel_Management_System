# 作者: ZengCheng
# 时间: 2023/5/12
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.utils.ModelForm import OrderModerForm
from app01.utils.Public_Function import order_number,format_time


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
        # 自定义添加随机订单号
        form.instance.order_number = order_number()
        # 当前登录系统的管理员ID
        form.instance.trade_admin_id = request.session['info']['id']
        # 添加创建时间
        form.instance.create_time = format_time()
        # 保存表单数据
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
