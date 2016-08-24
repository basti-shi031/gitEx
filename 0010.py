from PIL import Image, ImageDraw, ImageFont
import random

text = ''.join(random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789', 4))
mode = 'RGB'
fontName = 'verdana.ttf'


def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def create_identifying_code(strs, i):
    # 生成背景图片
    # 新建一张图片
    img = Image.new(mode, (400, 300), (255, 255, 255))
    #     生成噪点
    draw = ImageDraw.Draw(img)
    for x in range(400):
        for y in range(300):
            draw.point((x, y), randomColor())

    font = ImageFont.truetype(fontName, 80)
    fontWidth, fontHeight = font.getsize(strs)
    # 起始坐标
    x = (400 - fontWidth) / 2
    y = (400 - fontHeight) / 2
    length = len(strs)
    for a in strs:
        draw.text((x, y), a, randomColor(), font)
        x = fontWidth / length + x

    img.save(str(i) + ".jpg")


def randomText():
    return ''.join(random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789', 4))


if __name__ == '__main__':
    for i in range(50):
        create_identifying_code(randomText(), i)
