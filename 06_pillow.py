# http://www.mwsoft.jp/programming/computer_vision_with_python/1_1_pil.html
# coding: utf-8

from PIL import Image

img = Image.open("test.jpg")

gray_img = img.convert("L")

gray_img.save("hogehoge.jpg")
