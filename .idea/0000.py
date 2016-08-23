# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image,ImageDraw,ImageFont

def add_num(image):
    # 创建绘画对象
    draw = ImageDraw.Draw(image);
    # 获取图片大小
    width,height = image.size
    # 写字
    draw.text((width-100,0),'6')
    # 保存
    image.save('result.jpg','jpeg')


# 获取图片
image = Image.open('a.jpg')
# 添加数字
add_num(image)
