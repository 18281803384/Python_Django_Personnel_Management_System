# 作者: ZengCheng
# 时间: 2023/4/27
from django import forms


class Bootstrap_ModelForm(forms.ModelForm):
    bootstrap_exclude_field = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加属性
        for name, field in self.fields.items():
            # 如果该字段在排除的列表中则跳过
            if name in self.bootstrap_exclude_field:
                continue

            # 如果字段中有属性，则保留原来的属性，没有属性才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class Bootstrap_Form(forms.Form):
    bootstrap_exclude_field = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加属性
        for name, field in self.fields.items():
            # 如果该字段在排除的列表中则跳过
            if name in self.bootstrap_exclude_field:
                continue

            # 如果字段中有属性，则保留原来的属性，没有属性才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }