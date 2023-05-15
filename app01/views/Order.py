# 作者: ZengCheng
# 时间: 2023/5/12
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.ModelForm import OrderModerForm
from app01.utils.Paging_Module import Paging_Module
from app01.utils.Public_Function import order_number, format_time


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


# ------- 订单删除函数 ------- #
def order_delete(request):
    # 获取需要删除的订单ID
    delete_id = request.GET.get('delete_id')
    # 查询该数据在数据库是否存在
    exists = models.Order.objects.filter(id=delete_id).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在！"})
    # 删除该订单数据
    models.Order.objects.filter(id=delete_id).delete()
    return JsonResponse({"status": True})


# ------- 订单详情函数 ------- #
def order_detail(request):
    # 获取需要编辑的订单ID
    deit_id = request.GET.get('deit_id')
    # 获取该ID数据指定字段，返回为dict格式
    row_data = models.Order.objects.filter(id=deit_id).values('trade_name', 'trade_price', 'trade_status').first()
    if not row_data:
        return JsonResponse({"status": False, "error": "编辑失败，数据不存在！"})
    result = {
        "status": True,
        "data": row_data
    }
    return JsonResponse(result)
