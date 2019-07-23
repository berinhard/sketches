# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

colors = get_color_palette()

def setup():
    size(900, 900)
    strokeWeight(5)
    background(242)
    stroke(27)

def lado_coracao(w, h):
    altura_coracao = 425

    p1 = w / 2, h / 2 + altura_coracao
    p2 = w / 2, h / 2
    p3 = w / 2 - altura_coracao / 2, h / 2

    noFill()
    triangle(p1[0], p1[1],p2[0], p2[1],p3[0], p3[1])

    p_arc = w / 2 - altura_coracao / 4, h / 2
    arc(p_arc[0], p_arc[1], altura_coracao / 2, altura_coracao / 2, PI, TWO_PI)


def draw():
    for i in range(2, 17):
        background(242)
        num_points = i
        for i in range(num_points):
            angle = i * TWO_PI / num_points
            with pushMatrix():
                translate(width / 2, height / 2)
                rotate(angle)
                lado_coracao(0, 0)  # esquerdo
                with pushMatrix():
                    scale(-1, 1)
                    lado_coracao(0, 0)  # esquerd


        saveFrame(str(num_points) + ".png")