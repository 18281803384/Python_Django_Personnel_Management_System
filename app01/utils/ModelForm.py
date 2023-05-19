# 作者: ZengCheng
# 时间: 2023/4/27
from django import forms
from django.core.validators import RegexValidator, ValidationError

from app01 import models
from app01.utils.Bootstrap import Bootstrap_ModelForm
from app01.utils.Encryption import md5


# 员工修改 ---- ModelForm
class PersonnelAddModelForm(Bootstrap_ModelForm):
    personnel_name = forms.CharField(max_length=36, label="员工姓名")

    class Meta:
        model = models.Personnel
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    def clean_account(self):
        text_account = self.cleaned_data['account']
        exists = models.Personnel.objects.filter(account=text_account).exists()
        if exists:
            raise ValidationError("该用户已存在！")
        return text_account


# 员工修改 ---- ModelForm
class PersonnelEditModelForm(Bootstrap_ModelForm):
    personnel_name = forms.CharField(max_length=36, label="员工姓名")

    class Meta:
        model = models.Personnel
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]


# 靓号新增 ---- ModelForm
class PrettyAddModelForm(Bootstrap_ModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机格式错误！')]
    )

    class Meta:
        model = models.Pretty
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    # 验证方式2 钩子方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 查询表中指定数据是否存在，返回是布尔类型
        exists = models.Pretty.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在！')
        # 验证通过，用户输入的值就返回
        return txt_mobile


# 靓号修改 ---- ModelForm
class PrettyEditModelForm(Bootstrap_ModelForm):
    mobile = forms.CharField(
        label='手机号',
        disabled=True
    )

    class Meta:
        model = models.Pretty
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    # 钩子方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 查询表中排除本身id外指定数据是否存在，返回是布尔类型
        exists = models.Pretty.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在！')
        # 验证通过，用户输入的值就返回
        return txt_mobile


# 管理员新增 ---- ModelForm
class AdminAddModelForm(Bootstrap_ModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['admin_name', 'account', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        # 获取POST请求提交时输入时的数据
        password = self.cleaned_data.get('password')
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise ValidationError('密码不一致！')
        return confirm_password


# 管理员修改 ---- ModelForm
class AdminEditModelForm(Bootstrap_ModelForm):
    class Meta:
        model = models.Admin
        fields = ['admin_name']


# 管理员密码重置 ---- ModelForm
class AdminPsResetModelForm(Bootstrap_ModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['account', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        # 获取POST请求提交时输入时的数据
        password = self.cleaned_data.get('password')
        # 对数据进行md5加密
        md5_password = md5(password)
        # 验证md5加密后数据是否跟指定id数据的password字段数据一样
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_password).exists()
        # 如果一样，则抛出提示
        if exists:
            raise ValidationError('密码不能跟之前的一致！')
        # 不一样则返回数据
        return md5_password


# 任务新增 ---- ModelForm
class TaskManagerModelForm(Bootstrap_ModelForm):
    class Meta:
        model = models.TaskManager
        fields = ['level', 'task_title', 'task_details', 'task_head']
        widgets = {
            "task_details": forms.TextInput
        }


# 订单新增 ---- ModelForm
class OrderModerForm(Bootstrap_ModelForm):
    class Meta:
        model = models.Order
        # 排除一下字段，渲染其它所有字段
        exclude = ['order_number', 'trade_admin', 'create_time', 'update_time']


# 文件上传 ---- ModelForm
class upload_modelform(Bootstrap_ModelForm):
    class Meta:
        Bootstrap_ModelForm.bootstrap_exclude_field = ["city_logo"]

        model = models.ModelForm_Uploads
        # 排除一下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]
