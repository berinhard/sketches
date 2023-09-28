import py5

def draw_shape(points, curve=False):
    s = py5.create_shape()
    s.begin_shape()

    vertex_method = s.curve_vertex if curve else s.vertex

    vertex_method(points[0].x, points[0].y)
    for point in points:
        vertex_method(point.x, point.y)
    vertex_method(points[-1].x, points[-1].y)

    s.end_shape(py5.CLOSE)
    py5.shape(s)

