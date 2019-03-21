# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

TOTAL_FRAMES = 100
WIDTH, HEIGHT = 900, 900
WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
BLUE = color(55,189,202)
COMPLEMENTARY = BLUE

def get_gif_percent(total_frames, counter=None):
    counter = counter or frameCount
    return float(counter) % total_frames / total_frames


def setup():
    size(WIDTH, HEIGHT)
    strokeWeight(4)
    frameRate(24)


def draw():
    if frameCount > TOTAL_FRAMES:
        noLoop()

    background(BLACK)
    stroke(WHITE)
    noFill()

    percent = get_gif_percent(TOTAL_FRAMES)
    angle = easings.easeInOutSine(percent) * TWO_PI

    for y in range(height / 4, 3 * height / 4, 40):
        px, py = -2, y
        for x in range(-2, width + 2, 2):
            base_angle = x / 1000. * TWO_PI
            y_offset = sin(angle + base_angle)

            rate = map(x, 0, width, 0, 1)
            c = lerpColor(WHITE, COMPLEMENTARY, rate)
            stroke(c)

            y += y_offset
            line(x, y, px, py)
            px, py = x, y

    saveFrame("########.png")
