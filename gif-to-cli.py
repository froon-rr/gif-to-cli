#!/usr/bin/env python3

from PIL import Image
from colorit import color_back, color_front
import os
import time
import sys


def gifToCli(ima, x=75, y=32, s='#'):
    im = Image.open(ima)
    while True:
        i = 0
        try:
            while True:
                os.system("clear")
                i = i + 1
                im.seek(i)
                img = im
                img = img.resize((x, y))
                img = img.convert("RGB")
                # print(im.tell())
                for col in range(img.size[1]):
                    for row in range(img.size[0]):
                        print(color_front(s, img.getpixel((row, col))), end='')
                    print()
                time.sleep(0.06)
        except EOFError:
            pass

if len(sys.argv) == 1:
    print('укажите адрес gif файла (gif-to-cli /path/to/file.gif)')

elif len(sys.argv) == 2:
    gifToCli(sys.argv[1])

elif len(sys.argv) == 3:
    gifToCli(sys.argv[1], int(sys.argv[2]), int(sys.argv[2]))

elif len(sys.argv) == 4:
    gifToCli(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

elif len(sys.argv) == 5:
    gifToCli(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
