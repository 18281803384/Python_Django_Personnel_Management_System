# 作者: ZengCheng
# 时间: 2023/4/21
# 备注: 此处放着额外的公共方法
from datetime import datetime
import time
import random

from PIL import ImageDraw, ImageFont, ImageFilter, Image


# ------- 获取当前时间函数 ------- #
def format_time():
    times = time.time()
    local_time = time.localtime(times)
    correct_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return correct_time


# ------- 根据时间生成订单号 ------- #
def order_number():
    # 生成当前时间并格式化
    local_time = datetime.now().strftime("%Y%m%d%H%M%S")
    # 组合随机订单号
    random_order_number = local_time + str(random.randint(1000,9999))
    return random_order_number


# ------- 生成随机的图片验证码 ------- #
def check_code(width=120, height=30, char_length=5, font_file=r"app01/static/fonts/Monaco.ttf", font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text((i * width / char_length, h), char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
