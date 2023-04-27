# 作者: ZengCheng
# 时间: 2023/4/27
from django import forms


class Bootstrap_ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加属性
        for name, field in self.fields.items():
            # 如果字段中有属性，则保留原来的属性，没有属性才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = '请输入...'
                field.widget.attrs["style"] = "width: 500px"
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": '请输入...',
                    "style": "width: 500px"
                }