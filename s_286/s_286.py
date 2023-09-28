import py5

from be5.shapes import WithCenterShape
from be5.draw import draw_shape

SIZE = 900

shapes = []


def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    py5.background(15)
    x, y = py5.width / 2, py5.height / 2
    center = py5.Py5Vector(x, y)

    radius = list(range(10, 380, 10))
    num_points = 16
    shapes.extend([
        WithCenterShape(
            center,
            radius=r,
            num_points=num_points,
            radius_noise=(len(radius) - i) / len(radius),
            radius_off=40
        )
        for i, r in enumerate(sorted(radius, reverse=True))
    ])


def draw():
    r, g, b = (242, 38, 93)
    for i, shape in enumerate(shapes):
        rate = (len(shapes) - i) / len(shapes)

        off = int(py5.random(len(shapes)))
        points = list(shape.points)
        points = points[off:] + points[:off]
        print(points)

        w = py5.remap(rate, 0, 1, 1, 5)
        a = py5.remap(rate, 0, 1, 200, 80)
        #r = py5.remap(rate / 2, 0, .5, 82, 242) * -1
        g = py5.remap(rate, 0, 1, 70, 180)

        py5.stroke(r, g, b, a)
        py5.stroke(0, 0, 0, a)
        py5.stroke_weight(w)
        py5.fill(r,g,b)
        draw_shape(points, True)

    #py5.save_frame("rose.png")
    py5.no_loop()

py5.run_sketch()
