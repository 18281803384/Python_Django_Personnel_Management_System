# 作者: ZengCheng
# 时间: 2023/5/16
from django.http import JsonResponse
from django.shortcuts import render


# ------- 数据统计列表函数 ------- #
def echarts_list(request):
    return render(request, 'echarts_list.html')


# ------- 柱状图数据函数 ------- #
def echarts_bar_data(request):
    # 主标题文本
    title_text = 'ECharts Bar'
    # 图例项的名称
    legend_data = ['张三', '王五']
    # x坐标轴名称
    xAxis_data = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

    # 柱状图显示数据
    series = [
        {
            'name': '张三',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20, 30]
        },
        {
            'name': '王五',
            'type': 'bar',
            'data': [10, 6, 43, 20, 5, 25, 42]
        }
    ]

    result = {
        "status": True,
        "bar_data": {
            "title_text": title_text,
            "legend_data": legend_data,
            "xAxis_data": xAxis_data,
            "series": series
        }
    }

    return JsonResponse(result)


# ------- 折线图数据函数 ------- #
def echarts_line_data(request):
    title_text = 'ECharts Line'
    legend_data = ['xxA公司', 'xxB公司']
    xAxis_data = ['iPhone 8', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14', 'OPPO', '小米']
    series = [
        {
            'name': 'xxA公司',
            'data': [150, 230, 224, 218, 135, 147, 260],
            'type': 'line'
        },
        {
            'name': 'xxB公司',
            'data': [140, 150, 230, 245, 160, 284, 290],
            'type': 'line'
        }
    ]

    result = {
        "status": True,
        "line_data": {
            "title_text": title_text,
            "legend_data": legend_data,
            "xAxis_data": xAxis_data,
            "series": series
        }
    }

    return JsonResponse(result)


# ------- 饼状图数据函数 ------- #
def echarts_pie_data(request):
    series_data = [
        {"value": 1048, "name": '小米'},
        {"value": 735, "name": 'OPPO'},
        {"value": 580, "name": 'iPhone'},
        {"value": 484, "name": '华为'},
        {"value": 300, "name": 'VIVO'}
    ]

    result = {
        "status": True,
        "series_data": series_data
    }

    return JsonResponse(result)
