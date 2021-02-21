import math
from PIL import Image, ImageDraw, ImageFont

x=250 #центр полигона (x)
y=250 #центр полигона (y)
n=5   #число сторон полигона
r=200  #радиус окружности в которую вписываем полигон
#получаем координаты вершин
coords=[(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)]

img = Image.new("RGB",(500,500), (255,255,255))
draw = ImageDraw.Draw(img)

draw.polygon((coords), fill="lightblue",outline =(255,0,0))
unicode_font = ImageFont.truetype("arial.ttf", 22)
draw.text ((100,40), u'Это многоугольник', font=unicode_font, fill='red' )
img.show()