# 作者: ZengCheng
# 时间: 2023/5/16
from django.shortcuts import render


# ------- 数据统计列表函数 ------- #
def echarts_list(request):
    return render(request, 'echarts_list.html')