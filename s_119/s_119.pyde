# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Based in:
# Times Tables Cardioid
# Daniel Shiffman
# https://thecodingtrain.com/CodingChallenges/133-times-tables-cardioid.html
# https://youtu.be/bl3nc_a1nvs
# https://editor.p5js.org/codingtrain/present/gwcGb_NPm
from berin.save_frames import save_video_frames

WHITE = color(230)
BLACK = color(27, 27, 27)
RED = color(212, 32, 10, 42)
BLUE = color(55,189,182, 42)

def setup():
    size(900, 900)
    strokeWeight(1.5)
    noFill()

def get_vector(index, total, r, extra_rotation=0):
    angle = map(index % total, 0, total, 0, TWO_PI)
    vector = PVector.fromAngle(angle + extra_rotation)
    vector.mult(r)
    return vector

ordering = []

def draw():
    translate(width / 2, height / 2)
    background(BLACK)
    r = 400

    factor = map(noise(frameCount * 0.009), 0, 1, 0.1, 15)
    total = 300

    if not ordering:
        for i in range(total):
            ordering.append(random(1) > 0.5)

    for i in range(total):
        if ordering[i]:
            stroke(RED)
            point_1 = get_vector(i, total, r)
            point_2 = get_vector(i * factor, total, r)
            line(point_1.x, point_1.y, point_2.x, point_2.y)
            stroke(BLUE)
            point_1 = get_vector(i, total, r, PI)
            point_2 = get_vector(i * factor, total, r, PI)
            line(point_1.x, point_1.y, point_2.x, point_2.y)
        else:
            stroke(BLUE)
            point_1 = get_vector(i, total, r, PI)
            point_2 = get_vector(i * factor, total, r, PI)
            line(point_1.x, point_1.y, point_2.x, point_2.y)
            stroke(RED)
            point_1 = get_vector(i, total, r)
            point_2 = get_vector(i * factor, total, r)
            line(point_1.x, point_1.y, point_2.x, point_2.y)

    save_video_frames(12, 60 * 10)