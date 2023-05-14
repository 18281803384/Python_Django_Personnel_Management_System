# 作者: ZengCheng
# 时间: 2023/5/12
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.ModelForm import OrderModerForm
from app01.utils.Paging_Module import Paging_Module
from app01.utils.Public_Function import order_number,format_time


# ------- 订单列表函数 ------- #
def order_list(request):
    form = OrderModerForm()

    # 根据字典条件获取表中的数据，并以order_by进行排序，当字典为空时查询所有数据
    order_data = models.Order.objects.all().order_by('-id')

    # ------ 分页功能 start
    page_object = Paging_Module(request, order_data)
    # ------ 分页功能 end

    context = {
        "form": form,
        "order_data": page_object.page_queryset,
        "page_li_list_string": page_object.show_html()
    }
    return render(request, 'order_list.html', context)


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
