# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


class ContainedSquares(object):

    def __init__(self, x, y, size, reverse_colors=False):
        """
        v1 --- v2
        |       |
        |       |
        v4 --- v3
        """
        self.x, self.y, self.size = x, y, size
        self.vertices = [
            PVector(x, y),  # v1
            PVector(x + size, y),  # v2
            PVector(x + size, y + size),  # v3
            PVector(x, y + size),  # v4
        ]
        self.v1, self.v2, self.v3, self.v4 = self.vertices
        self.internal = PVector(x, y)
        self.reverse_colors = reverse_colors

    def update_internal_x(self, edge_percent):
        x = lerp(self.v1.x, self.v2.x, edge_percent)
        self.internal = PVector(x, self.internal.y)

    def update_internal_y(self, edge_percent):
        y = lerp(self.v1.y, self.v4.y, edge_percent)
        self.internal = PVector(self.internal.x, y)

    def update_internal(self, edge_percent):
        self.update_internal_x(edge_percent)
        self.update_internal_y(edge_percent)

    def get_all_shapes(self):
        colors = [color(235, 0, 235), color(235, 235, 0), color(235), color(0, 235, 235)]
        if self.reverse_colors:
            colors = [color(235), color(0, 235, 235), color(235, 0, 235),color(235, 235, 0)]

        return [
            RectByVertices([self.v1, PVector(self.internal.x, self.v1.y), self.internal, PVector(self.v1.x, self.internal.y)], colors[0]),
            RectByVertices([PVector(self.internal.x, self.v2.y), self.v2, PVector(self.v2.x, self.internal.y), self.internal], colors[1]),
            RectByVertices([self.internal, PVector(self.v3.x, self.internal.y), self.v3, PVector(self.internal.x, self.v3.y)], colors[2]),
            RectByVertices([PVector(self.v4.x, self.internal.y), self.internal, PVector(self.internal.x, self.v4.y), self.v4], colors[3]),
        ]

    def display(self):
        for shape in self.get_all_shapes():
            shape.display()


class RectByVertices(object):

    def __init__(self, vertices, r_color):
        self.vertices = vertices
        self.color = r_color

    def display(self):
        fill(self.color)
        draw_shape(self.vertices, end_shape_mode=CLOSE)


WIDTH, HEIGHT = 800, 800
squares_container = ContainedSquares(100, 100, WIDTH - 200)


def setup():
    size(WIDTH, HEIGHT)
    strokeWeight(8)
    stroke(27)

def draw():
    global squares_container
    background(27)

    total_frames = 125.0
    percent = (frameCount % total_frames) / total_frames
    squares_container.update_internal_x(easings.easeInSine(percent))
    squares_container.update_internal_y(easings.easeOutSine(percent))
    squares_container.display()

    if frameCount == total_frames:
        squares_container = ContainedSquares(100, 100, WIDTH - 200, reverse_colors=True)
    if frameCount <= total_frames * 2:
        saveFrame("####.png")