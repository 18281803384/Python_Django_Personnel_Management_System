# 作者: ZengCheng
# 时间: 2023/4/27
"""
自定义的分页组件

    调用方法：
    # ------ 分页功能 start
    page_object = Paging_Module()
    # ------ 分页功能 end


    <nav aria-label="...">
        <ul class="pagination">
            {{ page_li_list_string }}
        </ul>
    </nav>

"""
from django.utils.safestring import mark_safe


class Paging_Module(object):
    def __init__(self, request, queryset, default_num=10, page_param='page', plus_page=5):
        """
        :param request: 用于获取用户输入的页数
        :param queryset: 对数据库查询的对象
        :param default_num: 默认显示条数
        :param page_param: 默认接受前端参数
        :param plus_page: 默认前后页显示页数
        """
        # 校验页数格式
        get_page = request.GET.get(page_param, '1')
        if get_page.isdecimal():
            get_page = int(get_page)
        else:
            get_page = 1
        # 获取get请求传入的页数
        self.get_page = get_page
        # 页面默认显示条数
        self.default_num = default_num
        # 开始区间 = （请求页数 - 1）* 默认数量
        self.start_num = (self.get_page - 1) * self.default_num
        # 结束区间 = 请求页数 * 默认数量
        self.end_num = self.get_page * self.default_num
        # 数据查询区间
        self.page_queryset = queryset[self.start_num: self.end_num]
        total_count = queryset.count()
        total_page, remain = divmod(total_count, self.default_num)
        if remain != 0:
            total_page += 1
        # 根据数据量计算出总页数
        self.total_count = total_page
        # 计算出展示当前页前后页码数
        self.plus_page = plus_page

    def show_html(self):
        # 如果数据量比较少，没有到达前后页总数
        if self.total_count <= (2 * self.plus_page) + 1:
            start_page = 1
            end_page = self.total_count
        else:
            # 如果请求页 <= 前后页数
            if self.get_page <= self.plus_page:
                start_page = 1
                end_page = (2 * self.plus_page) + 1
            else:
                # 如果请求页 + 前后页数 > 总页数
                if self.get_page + self.plus_page > self.total_count:
                    start_page = self.total_count - (2 * self.plus_page)
                    end_page = self.total_count
                else:
                    start_page = self.get_page - self.plus_page
                    end_page = self.get_page + self.plus_page

        # 创建一个空列表，用于存储循环生成li标签
        page_li_list = []
        # 首页标签
        if self.get_page != 1:
            first_page_li = '<li><a href="?page={}">首页</a></li>'.format(1)
        else:
            first_page_li = '<li class="previous disabled"><a href="#">首页</a></li>'
        page_li_list.append(first_page_li)
        # 上一页标签
        if self.get_page > 1:
            previous_page_li = '<li><a href="?page={}">上一页</a></li>'.format(self.get_page - 1)
        else:
            previous_page_li = '<li class="previous disabled"><a href="#">上一页</a></li>'
        page_li_list.append(previous_page_li)
        # 根据数据量循环生成li标签页数
        for i in range(start_page, end_page + 1):
            if i == self.get_page:
                page_li = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                page_li = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_li_list.append(page_li)
        # 下一页标签
        if self.get_page < self.total_count:
            previous_page_li = '<li><a href="?page={}">下一页</a></li>'.format(self.get_page + 1)
        else:
            previous_page_li = '<li class="previous disabled"><a href="#">下一页</a></li>'
        page_li_list.append(previous_page_li)
        # 尾页标签
        if self.get_page != self.total_count and self.total_count != 0:
            last_page_li = '<li><a href="?page={}">尾页</a></li>'.format(self.total_count)
        else:
            last_page_li = '<li class="previous disabled"><a href="#">尾页</a></li>'
        page_li_list.append(last_page_li)
        jump_page_li = '''
                <li>
                    <form style="float: left; margin-left: -1px" method="get">
                        <input name="page" style="position: relative; float: left; display: inline-block; width: 120px" type="text" class="form-control" placeholder="请输入页码...">
                        <button type="submit" class="btn btn-default">跳转</button>
                    </form>
                </li>
            '''
        page_li_list.append(jump_page_li)

        # 将list数据转化为string数据，并mark_safe函数让HTML可渲染
        page_li_list_string = mark_safe("".join(page_li_list))

        return page_li_list_string