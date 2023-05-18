# 作者: ZengCheng
# 时间: 2023/5/8
from django import forms

from app01.utils.Bootstrap import Bootstrap_Form
from app01.utils.Encryption import md5


class LoginForm(Bootstrap_Form):
    account = forms.CharField(label='用户名', widget=forms.TextInput)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(render_value=True))
    image_code = forms.CharField(label='图片验证码', widget=forms.TextInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)


class upload_form(Bootstrap_Form):
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    head_sculpture = forms.FileField(label="头像")

    Bootstrap_Form.bootstrap_exclude_field = ['head_sculpture']