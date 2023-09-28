import py5

from contextlib import contextmanager

@contextmanager
def draw_at_center():
    """
    Move the 0, 0 to the center of the sketch
    """
    try:
        py5.translate(py5.width/2, py5.height/2)
        yield
    finally:
        pass


def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * py5.cos(angle)
    y = y0 + r * py5.sin(angle)

    return py5.Py5Vector(x, y)
