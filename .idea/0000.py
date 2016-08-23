from PIL import Image,ImageDraw,ImageFont

def add_num(image):
    draw = ImageDraw.Draw(image);
    width,height = image.size
    draw.text((width-100,0),'6')
    image.save('result.jpg','jpeg')


image = Image.open('a.jpg')
add_num(image)
