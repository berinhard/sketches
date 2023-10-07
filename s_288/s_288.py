import random

import py5

from be5.shapes import TriSquare as BaseTriSquare

SIZE = 900
NUM_CELLS = 10
GRID_SIZE = SIZE // NUM_CELLS
SHAPES = {}


BACKGROUND = (42, 42, 42)
LINE = (220, 220, 220, 10)
#C1 = (54, 169, 27)
C1 = (74, 94, 206)
C2 = (21, 21, 21)

COLORS = [C1, C2]

class TriSquare(BaseTriSquare):


    def draw(self):
        py5.stroke_weight(5)
        py5.stroke(*LINE)

        c = COLORS[:]
        random.shuffle(c)

        py5.fill(*c[0])
        py5.triangle(self.v1.x, self.v1.y, self.v2.x, self.v2.y, self.v3.x, self.v3.y)

        py5.fill(*c[1])
        py5.triangle(self.v1.x, self.v1.y, self.v3.x, self.v3.y, self.v4.x, self.v4.y)



def populate_shapes():
    global SHAPES

    py5.background(*BACKGROUND)
    SHAPES = {}

    GRID_SIZE = (SIZE - 300) // NUM_CELLS
    print(GRID_SIZE)
    start = 0
    for i in range(start, NUM_CELLS + 1):
        for j in range(start, NUM_CELLS + 1):
            up_coord = (i, j - 1)
            left_coord = (i - 1, j)

            up_shape = SHAPES.get(up_coord)
            left_shape = SHAPES.get(left_coord)
            if j == 0 and i == 0:
                up_shape = None
            elif i == 0:
                left_shape = None


            # DEFAULT VALUES
            x = i * GRID_SIZE
            y = j * GRID_SIZE
            base = py5.random(1, 5)
            off_x = py5.random(GRID_SIZE / base, GRID_SIZE)
            off_y = py5.random(GRID_SIZE / base, GRID_SIZE)
            x_off = x + off_x
            y_off = y + off_y
            v1 = py5.Py5Vector(x, y)
            v2 = py5.Py5Vector(x_off, y)
            v3 = py5.Py5Vector(x_off, y_off)
            v4 = py5.Py5Vector(x, y_off)

            if up_shape:
                v1 = up_shape.v4
                v2 = up_shape.v3
            else:  # TODO FIX THIS RENDERING!!!!!
                off_x = py5.random(GRID_SIZE / base, GRID_SIZE)
                off_y = py5.random(GRID_SIZE / base, GRID_SIZE)
                v1.x += py5.remap(base, 1, 5, GRID_SIZE / base, 0)
                v1.y += py5.remap(base, 1, 5, -GRID_SIZE / base, 0)
                v2.x += py5.remap(base, 1, 5, GRID_SIZE / base, 0)
                v2.y += py5.remap(base, 1, 5, -GRID_SIZE / base, 0)

            if left_shape:
                v4 = left_shape.v3
                v1 = left_shape.v2
            else:
                v4.x += py5.remap(base, 1, 5, -GRID_SIZE/base, 0)
                v4.y += py5.remap(base, 1, 5, 0, GRID_SIZE/base)
                v1.x += py5.remap(base, 1, 5, -GRID_SIZE/base, 0)
                v1.y += py5.remap(base, 1, 5, 0, GRID_SIZE/base)


            if py5.random(1) > 0.1:
                SHAPES[(i, j)] = (
                    TriSquare(v1, v2, v3, v4)
                )

def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    populate_shapes()

def draw():
    with py5.push():
        py5.translate(150, 150)
        for shape in SHAPES.values():
            shape.draw()

    if py5.is_key_pressed:
        if py5.key in ['s', 'S']:
            py5.save_frame("cover03.png")
        elif py5.key in ['n', "N"]:
            populate_shapes()


py5.run_sketch()
