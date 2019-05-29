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
    background(27)
    for x in x_values:
        for y in y_values:
            for z in z_values:
                cubes.append(InnerCube(x, y, z, prob=random(1)))


class InnerCube(object):

    def __init__(self, x, y, z, prob):
        self.x = x
        self.y = y
        self.z = z
        self.prob = prob
        self.shine = random(2, 8)

    def display(self):
        if noise(frameCount * 0.01) ** 4 < self.prob:
            return

        r = map(self.x, -200, main_cube_size - 200, 0, 255)
        g = map(self.y, -200, main_cube_size - 200, 0, 255)
        b = map(self.z, -200, main_cube_size - 200, 0, 255)
        stroke(230, 230, 230, 30)
        noFill()
        shininess(self.shine)

        fill(r, g, b)
        with pushMatrix():
            rotateX(frameCount * 0.01)
            rotateY(frameCount * 0.01)
            rotateZ(frameCount * 0.01)
            translate(self.x, self.y, self.z)
            box(inner_cube_size)


def draw():
    strokeWeight(5)
    stroke(238, 238, 238, 30)

    directionalLight(
        map(noise(frameCount * 0.08), 0, 1, 40, 255),
        map(noise(frameCount * 0.02), 0, 1, 40, 255),
        map(noise(frameCount * 0.042), 0, 1, 40, 255),
        0, 0, -10
    )

    translate(400, 400, map(noise(frameCount * 0.2), 0, 1, -100, 100))
    for cube in cubes:
        cube.display()

    save_video_frames(24, 60)