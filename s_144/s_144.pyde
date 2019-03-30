
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin import easings
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from random import choice

easings_func = [
    easings.easeInQuad,
    easings.easeOutQuad,
    easings.easeInOutQuad,
    easings.easeInCubic,
    easings.easeOutCubic,
    easings.easeInOutCubic,
    easings.easeInQuart,
    easings.easeOutQuart,
    easings.easeInOutQuart,
    easings.easeInQuint,
    easings.easeOutQuint,
    easings.easeInOutQuint,
    easings.easeInSine,
    easings.easeOutSine,
    easings.easeInOutSine,
    easings.easeInExpo,
    easings.easeOutExpo,
    easings.easeInOutExpo,
    easings.easeInCirc,
    easings.easeOutCirc,
    easings.easeInOutCirc,
]

WHITE = color(241, 241, 241)
BLACK = color(27, 27, 27)
COMPLEMENTARY = color(218, 36, 89)

def get_gif_percent(total_frames, counter=None):
    counter = counter or frameCount
    if float(counter) / total_frames == 1:
        return 1.0
    return float(counter) % total_frames / total_frames

WIDTH, HEIGHT = 900.0, 900.0
total_frames = 100


class GifLine(object):

    def __init__(self, y, line_size, easing=None):
        self.x = 0
        self.y = y
        self.line_size = line_size
        self.offset = line_size / 2.0
        self.easing = easing or easings.linear

    def update(self, percent):
        self.x = width * self.easing(percent)

    def draw(self):
        x1 = self.x - self.offset
        x2 = self.x + self.offset
        #w = map(abs(width / 2 - self.x), 0, width / 2, 50, 10)
        strokeWeight(2)
        stroke(WHITE)
        line(x1, self.y, x2, self.y)

lines = []

def setup():
    size(int(WIDTH), int(HEIGHT))
    background(BLACK)

    for y in range(0, int(HEIGHT + 90), 90):
        line_size = choice(range(20, 200, 10))
        easing_func = choice(easings_func)
        lines.append(GifLine(y, line_size, easing_func))

    #frameRate(24)


counter = 0
def draw():
    global counter
    counter += 1

    background(BLACK)

    percent = get_gif_percent(total_frames)

    print percent
    for l in lines:
        l.update(percent)
        l.draw()

    #rect(0, 0, 20, height)
    #rect(width - 20, 0, 20, height)

    #saveFrame("####.png")
    #if counter == total_frames:
    #    noLoop()