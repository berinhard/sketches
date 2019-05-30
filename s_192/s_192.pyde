# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

inner_cube_size = 40
main_cube_size = 400
cubes = []

x_values = range(-200, main_cube_size - 200, inner_cube_size)
y_values = range(-200, main_cube_size - 200, inner_cube_size)
z_values = range(-200, main_cube_size - 200, inner_cube_size)

def setup():
    size(800, 800, P3D)
    background(27, 27, 27, 30)
    for x in x_values:
        for y in y_values:
            for z in z_values:
                cubes.append(InnerCube(x, y, z, prob=random(1)))
    #frameRate(36)


class InnerCube(object):

    def __init__(self, x, y, z, prob):
        self.x = x
        self.y = y
        self.z = z
        self.prob = prob

    def display(self):
        if noise(frameCount * 0.01) ** 4 < self.prob:
            return
        noFill()

        with pushMatrix():
            rotateX(frameCount * 0.01)
            rotateY(frameCount * 0.01)
            rotateZ(frameCount * 0.01)
            translate(self.x, self.y, self.z)
            box(inner_cube_size)


def draw():
    fill(27, 27, 27, 50)
    noStroke()
    box(width * 2)

    noFill()
    strokeWeight(3)
    stroke(238, 238, 238, 50)

    translate(400, 400, 0)
    for cube in cubes:
        cube.display()

    #save_video_frames(60, 36)