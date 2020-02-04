# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import randrange
from PIL import Image, ImageDraw

WIDTH = 1024
HEIGHT = 1024
CELL_SIZE = 16  #pixels

final_image = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(final_image)

for x in range(0, WIDTH, CELL_SIZE):
    for y in range(0, HEIGHT, CELL_SIZE):
        # x, y are used to pick the cell's upper-left corner position

        r, g, b = randrange(255), randrange(255), randrange(255)
        for sx in range(x, x + CELL_SIZE):
            for sy in range(y, y + CELL_SIZE):
                # sx, sy are used to address each one of the cell's pixels
                final_image.putpixel((sx, sy), (r, g, b))

final_image.save('out.png')
