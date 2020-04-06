# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

import itertools
from random import choice

base = 425
COLORS = get_color_palette()

def setup():
    size(900, 900)
    background(242)
    strokeWeight(2)
    stroke(0)
    rectMode(CENTER)
    blendMode(EXCLUSION)

def keyPressed():
    blend_map = {
        "1": BLEND,# - linear interpolation of colors: C = A*factor + B.  This is the default.
        "2": ADD,# - additive blending with white clip: C = min(A*factor + B, 255)
        "3": SUBTRACT,# - subtractive blending with black clip: C = max(B - A*factor, 0)
        "4": DARKEST,# - only the darkest color succeeds: C = min(A*factor, B)
        "5": LIGHTEST,# - only the lightest color succeeds: C = max(A*factor, B)
        "6": DIFFERENCE,# - subtract colors from underlying image.
        "7": EXCLUSION,# - similar to DIFFERENCE, but less extreme.
        "8": MULTIPLY,# - multiply the colors, result will always be darker.
        "9": SCREEN,# - opposite multiply, uses inverse values of the colors.
        "q": REPLACE,# - the pixels entirely replace the others and don't utilize alpha (transparency) values
    }
    mode = blend_map.get(key, None)
    if mode:
        blendMode(mode)
    elif key == 's':
        saveFrame('######.png')


def draw():
    translate(width / 2, height / 2)
    background(240)
    colors = itertools.cycle(COLORS)

    x, y = 0, 0
    s1, s2, s3, s4 = [
        PVector(x - base, y - base),
        PVector(x + base, y - base),
        PVector(x + base, y + base),
        PVector(x - base, y + base),
    ]

    i1, i2, i3, i4 = [
        PVector(x, y - base),
        PVector(x + base / 2, y),
        PVector(x, y + base),
        PVector(x - base / 2, y),
    ]

    fill(next(colors))
    draw_shape([s1, i1, s2, s3, i3, s4], end_shape_mode=CLOSE)  # BASE

    # CIRCLES
    fill(next(colors))
    ellipse(i4.x, i4.y, base, base)
    fill(next(colors))
    ellipse(i2.x, i2.y, base, base)

    # TRIANGLES
    fill(next(colors))
    draw_shape([i1, i2, i4], end_shape_mode=CLOSE)
    fill(next(colors))
    draw_shape([i3, i2, i4], end_shape_mode=CLOSE)

    fill(next(colors))
    draw_shape([s1, i1, i4], end_shape_mode=CLOSE)
    draw_shape([i3, i2, s3], end_shape_mode=CLOSE)

    fill(next(colors))
    draw_shape([i1, i2, s2], end_shape_mode=CLOSE)
    draw_shape([s4, i4, i3], end_shape_mode=CLOSE)

    #noLoop()