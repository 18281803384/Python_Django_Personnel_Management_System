import time
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from app01 import models, public

# Create your views here.

""" ++++++++++++++++++++++++++++++++++++++++++ 部门管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 部门列表函数 ------- #
def department_list(request):
    # 查询部门表中的所有数据
    department_data = models.Department.objects.all()
    # 传入部门数据并渲染页面
    return render(request, "department_list.html", {"department_data": department_data})


# ------- 新增部门函数 ------- #
def department_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 跳转到部门新增页面
        return render(request, "department_add.html")

    # 获取POST请求协议的数据
    department_name = request.POST.get('department_name')
    if department_name == '':
        # 跳转到部门新增页面
        return render(request, "department_add.html", {"message": "请输入部门名称！"})
    # 在表中写入数据
    models.Department.objects.create(department_name=department_name, create_time=public.format_time())
    # 重定向到部门列表页面
    return redirect('/department/list')


# ------- 部门删除函数 ------- #
def department_delete(request, department_id):
    # 删除部门表指定部门id的数据
    models.Department.objects.filter(id=department_id).delete()
    # 重定向到部门列表页面
    return redirect('/department/list')


# ------- 部门修改函数 ------- #
def department_edit(request, department_id):
    department_data = models.Department.objects.filter(id=department_id).first()
    # 如果请求协议为GET
    if request.method == 'GET':
        return render(request, 'department_edit.html', {"department_data": department_data})

    # 获取POST请求协议的数据
    new_department_name = request.POST.get('department_name')
    if new_department_name == '':
        # 跳转到部门修改页面
        return render(request, 'department_edit.html', {"department_data": department_data})
    # 在表中修改数据
    models.Department.objects.filter(id=department_id).update(department_name=new_department_name,
                                                              update_time=public.format_time())
    # 重定向到部门列表页面
    return redirect('/department/list')


""" ++++++++++++++++++++++++++++++++++++++++++ 员工管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 员工列表函数 ------- #
def personnel_list(request):
    # 查询员工表中的所有数据
    personnel_data = models.Personnel.objects.all()
    # 传入员工数据并渲染页面
    return render(request, "personnel_list.html", {"personnel_data": personnel_data})


# ------- 员工添加函数 ------- #
def personnel_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        data = {
            "department_info": models.Department.objects.all(),
            "gender_choices": models.Personnel.gender_choices
        }
        # 传入数据并渲染页面
        return render(request, 'personnel_add.html', data)

    # 获取POST请求协议的数据
    personnel_name = request.POST.get('personnel_name')
    department = request.POST.get('department')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    salary = request.POST.get('salary')

    # 在表中写入数据
    models.Personnel.objects.create(personnel_name=personnel_name, department_id=department, gender=gender, age=age,
                                    salary=salary, create_time=public.format_time())
    # 重定向到部门列表页面
    return redirect('/personnel/list')


# ============= ModelForm start ============= #
from django import forms


class PersonnelModelForm(forms.ModelForm):
    personnel_name = forms.CharField(min_length=4, label="员工姓名")

    class Meta:
        model = models.Personnel
        fields = ["personnel_name", "department", "gender", "age", "salary"]

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        super(PersonnelModelForm, self).__init__(*args, **kwargs)
        # 循环找到所有的插件，添加 class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label, "style": "width: 500px"}


# ============= ModelForm end ============= #

# ------- 员工添加函数 基于ModelForm ------- #
def personnel_model_form_add(request):
    # 如果请求协议为GET
    if request.method == 'GET':
        # 实例化类
        form = PersonnelModelForm()
        # 传入数据并渲染页面
        return render(request, 'personnel_model_form_add.html', {"form": form})

    # 用户提交的数据进行校验
    form = PersonnelModelForm(data=request.POST)
    # 如果数据合法
    if form.is_valid():
        form.instance.create_time = public.format_time()
        # 保存数据到表中
        form.save()
        # 重定向到部门列表页面
        return redirect('/personnel/list')
    # 数据校验失败，则继续跳转到页面显示错误信息
    return render(request, 'personnel_model_form_add.html', {"form": form})


# ------- 员工修改函数 ------- #
def personnel_edit(request, personnel_id):
    row_personnel = models.Personnel.objects.filter(id=personnel_id).first()

    if request.method == 'GET':
        # 实例化类
        form = PersonnelModelForm(instance=row_personnel)
        # 传入数据并渲染页面
        return render(request, 'personnel_edit.html', {"form": form})

    # instance指定数据
    form = PersonnelModelForm(data=request.POST, instance=row_personnel)
    if form.is_valid():
        # 额外保存另外的值
        form.instance.update_time = public.format_time()
        # 保存数据到表中
        form.save()
        # 重定向到部门列表页面
        return redirect('/personnel/list')

    # 数据校验失败，则继续跳转到页面显示错误信息
    return render(request, 'personnel_edit.html', {"form": form})


# ------- 员工删除函数 ------- #
def personnel_delete(request, personnel_id):
    # 删除员工表指定员工id的数据
    models.Personnel.objects.filter(id=personnel_id).delete()
    # 重定向到部门列表页面
    return redirect('/personnel/list')


""" ++++++++++++++++++++++++++++++++++++++++++ 靓号管理页面 ++++++++++++++++++++++++++++++++++++++++++ """


# ------- 靓号列表函数 ------- #
def pretty_list(request):
    # ------ 查询功能 start
    data_dict = {}
    # 获取get请求传来的数据
    search_data = request.GET.get('search', '')
    # 如果有数据，则添加至字典中
    if search_data:
        data_dict["mobile__contains"] = search_data
    # ------ 查询功能 end

    # ------ 分页功能 start
    # 根据条件查询Pretty表的数据总条数
    pretty_count = models.Pretty.objects.filter(**data_dict).all().count()
    # 页面默认显示条数
    default_num = 10
    # divmod()函数取商和余
    total_page, remain = divmod(pretty_count, default_num)
    if remain != 0:
        # 根据数据量计算出总页数
        total_page += 1

    # 获取get请求传入的页数
    get_page = int(request.GET.get('page', '1'))
    # 开始区间 = （请求页数 - 1）* 默认数量
    start_num = (get_page - 1) * default_num
    # 结束区间 = 请求页数 * 默认数量
    end_num = get_page * default_num
    # 计算出展示当前页的前5页和后5页
    plus_page = 3
    # 如果数据量比较少，没有到达前后页总数
    if total_page <= (2 * plus_page) + 1:
        start_page = 1
        end_page = total_page
    else:
        # 如果请求页 <= 前后页数
        if get_page <= plus_page:
            start_page = 1
            end_page = (2 * plus_page) + 1
        else:
            # 如果请求页 + 前后页数 > 总页数
            if get_page + plus_page > total_page:
                start_page = total_page - (2 * plus_page)
                end_page = total_page
            else:
                start_page = get_page - plus_page
                end_page = get_page + plus_page

    # 创建一个空列表，用于存储循环生成li标签
    page_li_list = []
    # 首页标签
    if get_page != 1:
        first_page_li = '<li><a href="?page={}">首页</a></li>'.format(1)
    else:
        first_page_li = '<li class="previous disabled"><a href="#">首页</a></li>'
    page_li_list.append(first_page_li)
    # 上一页标签
    if get_page > 1:
        previous_page_li = '<li><a href="?page={}">上一页</a></li>'.format(get_page - 1)
    else:
        previous_page_li = '<li class="previous disabled"><a href="#">上一页</a></li>'
    page_li_list.append(previous_page_li)
    # 根据数据量循环生成li标签页数
    for i in range(start_page, end_page + 1):
        if i == get_page:
            page_li = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            page_li = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_li_list.append(page_li)
    # 下一页标签
    if get_page < total_page:
        previous_page_li = '<li><a href="?page={}">下一页</a></li>'.format(get_page + 1)
    else:
        previous_page_li = '<li class="previous disabled"><a href="#">下一页</a></li>'
    page_li_list.append(previous_page_li)
    # 尾页标签
    if get_page != total_page:
        last_page_li = '<li><a href="?page={}">尾页</a></li>'.format(total_page)
    else:
        last_page_li = '<li class="previous disabled"><a href="#">尾页</a></li>'
    page_li_list.append(last_page_li)

    # 将list数据转化为string数据，并mark_safe函数让HTML可渲染
    page_li_list_string = mark_safe("".join(page_li_list))

    # ------ 分页功能 end

    # 根据字典条件获取表中的数据，并以order_by进行排序，当字典为空时查询所有数据
    pretty_data = models.Pretty.objects.filter(**data_dict).order_by('id')[start_num: end_num]
    # 传入数据并渲染页面显示
    return render(request, 'pretty_list.html',
                  {"pretty_data": pretty_data, "search_data": search_data, "page_li_list_string": page_li_list_string})


# ============= PrettyAddModelForm start ============= #
from django.core.validators import RegexValidator, ValidationError


class PrettyAddModelForm(forms.ModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机格式错误！')]
    )

    class Meta:
        model = models.Pretty
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    def __init__(self, *args, **kwargs):
        super(PrettyAddModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label, "style": "width: 500px"}

    # 验证方式2 钩子方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 查询表中指定数据是否存在，返回是布尔类型
        exists = models.Pretty.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在！')
        # 验证通过，用户输入的值就返回
        return txt_mobile


# ============= PrettyAddModelForm end ============= #

# ------- 靓号添加函数 ------- #
def pretty_add(request):
    if request.method == 'GET':
        form = PrettyAddModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyAddModelForm(data=request.POST)
    if form.is_valid():
        form.instance.create_time = public.format_time()
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_add.html', {"form": form})


# ============= PrettyEditModelForm start ============= #
class PrettyEditModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label='手机号',
        disabled=True
    )

    class Meta:
        model = models.Pretty
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    def __init__(self, *args, **kwargs):
        super(PrettyEditModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label, "style": "width: 500px"}

    # 钩子方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 查询表中排除本身id外指定数据是否存在，返回是布尔类型
        exists = models.Pretty.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在！')
        # 验证通过，用户输入的值就返回
        return txt_mobile


# ============= PrettyEditModelForm end ============= #


# ------- 靓号修改函数 ------- #
def pretty_edit(request, pretty_id):
    row_pretty = models.Pretty.objects.filter(id=pretty_id).first()
    if request.method == 'GET':
        form = PrettyEditModelForm(instance=row_pretty)
        return render(request, 'pretty_edit.html', {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_pretty)
    if form.is_valid():
        form.instance.update_time = public.format_time()
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_edit.html', {"form": form})


# ------- 靓号删除函数 ------- #
def pretty_delete(request, pretty_id):
    models.Pretty.objects.filter(id=pretty_id).delete()
    return redirect('/pretty/list')
