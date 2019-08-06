#!/usr/bin/env python

import PIL.Image
import sys

imageFile = sys.argv[1] if len(sys.argv) > 1 else "Chicken.png"

image = PIL.Image.open(imageFile)

imageString = b''
pixels = image.load()

for y in range(image.height):
  for x in range(image.width):
    r = (pixels[x,y][0] >> 0x3) & 0x3F
    g = (pixels[x,y][1] >> 0x3) & 0x3F
    b = (pixels[x,y][2] >> 0x3) & 0x3F
    color = 0x8000
    color |= r << 0xA
    color |= g << 0x5
    color |= b << 0x0
    msb = (color & 0xFF00) >> 0x8
    lsb = (color & 0x00FF)
    print(hex(color))
    # print(hex(msb))
    # print(bytes([msb]))
    # print (hex(lsb))
    # print (chr(msb)+chr(lsb))
    imageString += bytes([msb])
    imageString += bytes([lsb])

# print(imageString.decode('utf-16'))