# 作者: ZengCheng
# 时间: 2023/5/5
# 备注: MD5加密
from django.conf import settings
import hashlib


# 对制定字符串进行md5加密
def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()