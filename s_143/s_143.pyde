# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin import easings
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine

WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
COMPLEMENTARY = color(218, 36, 89)

def get_gif_percent(total_frames):
    return float(frameCount) % total_frames / total_frames

frame_rate = 100
going_flag = True
all_percents = [float(i) / frame_rate for i in range(1, frame_rate + 1)]
WIDTH, HEIGHT = 900, 900
params = [
    (
        map(abs(easings.easeInSine(percent)), 0, 1, -10, WIDTH + 10),  # x
        map(abs(0.5 - easings.easeInSine(percent)), 0, 0.5, HEIGHT / 2 - 10, 0),  # h
    ) for percent in all_percents
]


def setup():
    size(WIDTH, HEIGHT)
    strokeWeight(2)
    background(WHITE)


def draw():
    index = frameCount % frame_rate
    print(all_percents)
    print(params)
    #percents = get_gif_percent(100)

    global going_flag

    if index == 0:
        going_flag = not going_flag

    stroke(WHITE)
    if going_flag:
        x, h = params[index]
        fill(BLACK)
        rect(x, 0, 20, h)
        fill(COMPLEMENTARY)
        rect(0, x - 10, h, 20)
        fill(BLACK)
        rect(x, height, 20, -h)
        fill(COMPLEMENTARY)
        rect(width, x - 10, -h + 10, 20)
    else:
        background(WHITE)
        for x, h in params[index:-1]:
            fill(BLACK)
            rect(x, 0, 20, h)
            fill(COMPLEMENTARY)
            rect(0, x - 10, h, 20)
            fill(BLACK)
            rect(x, height, 20, -h)
            fill(COMPLEMENTARY)
            rect(width, x - 10, -h + 10,  20)

    if frameCount > 200:
        noLoop()
    saveFrame("####.png")


    # if frameCount >= 101:
    #     noLoop()
    #saveFrame(nf(frameCount, 4) + ".png")