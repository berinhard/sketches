# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine

WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)

def get_gif_percent(total_frames):
    return float(frameCount) % total_frames / total_frames

def setup():
    size(500, 500)
    strokeWeight(2)


def draw():
    percent = get_gif_percent(100)

    with draw_at_center():
        r = map(abs(0.5 - percent), 0, 0.5, 0, 200)

        if percent >= 0.5:
            stroke(WHITE)
            fill(WHITE)
            background(BLACK)
        else:
            stroke(BLACK)
            fill(BLACK)
            background(WHITE)

        ellipse(0, 0, r, r)
        line(-250, 0 - r / 2, 250, 0 - r / 2)
        line(-250, 0 + r / 2, 250, 0 + r / 2)
        line(0 - r / 2, -250, 0 - r / 2, 250)
        line(0 + r / 2, -250, 0 + r / 2, 250)

    # if frameCount >= 101:
    #     noLoop()
    #saveFrame(nf(frameCount, 4) + ".png")