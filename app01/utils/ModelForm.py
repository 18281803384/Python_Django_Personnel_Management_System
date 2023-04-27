# 作者: ZengCheng
# 时间: 2023/4/27
from django import forms
from app01 import models
from django.core.validators import RegexValidator, ValidationError

from app01.utils.Bootstrap_ModelForm import Bootstrap_ModelForm


class PersonnelModelForm(Bootstrap_ModelForm):
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


class AdminModelForm(Bootstrap_ModelForm):
    admin_name = forms.CharField(max_length=36, label="管理员名称")

    class Meta:
        model = models.Admin
        # 排除以下字段，渲染其它所有字段
        exclude = ["create_time", "update_time"]

    def clean_account(self):
        text_account = self.cleaned_data['account']
        exists = models.Personnel.objects.filter(account=text_account).exists()
        if exists:
            raise ValidationError("该管理员已存在！")
        return text_account
