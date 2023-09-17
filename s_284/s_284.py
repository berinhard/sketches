import py5

from shapes import TriSquare

SIZE = 900
NUM_CELLS = 10
GRID_SIZE = SIZE // NUM_CELLS
SHAPES = {}

def populate_shapes():
    global SHAPES

    SHAPES = {}
    for i in range(-1, NUM_CELLS + 1):
        for j in range(-1, NUM_CELLS + 1):
            up_coord = (i, j - 1)
            left_coord = (i - 1, j)

            up_shape = SHAPES.get(up_coord)
            left_shape = SHAPES.get(left_coord)

            # DEFAULT VALUES
            x = i * GRID_SIZE
            y = j * GRID_SIZE
            base = py5.random(1, 6)
            x_off = x + py5.random(GRID_SIZE / base, GRID_SIZE)
            y_off = y + py5.random(GRID_SIZE / base, GRID_SIZE)
            v1 = py5.Py5Vector(x, y)
            v2 = py5.Py5Vector(x_off, y)
            v3 = py5.Py5Vector(x_off, y_off)
            v4 = py5.Py5Vector(x, py5.height)

            if up_shape:
                v1 = up_shape.v4
                v2 = up_shape.v3
            if left_shape:
                v4 = left_shape.v3

            SHAPES[(i, j)] = (
                TriSquare(v1, v2, v3, v4)
            )

def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    py5.background(242)
    populate_shapes()

def draw():
    for shape in SHAPES.values():
        shape.draw()

    py5.save_frame("cover.png")
    py5.no_loop()

py5.run_sketch()
