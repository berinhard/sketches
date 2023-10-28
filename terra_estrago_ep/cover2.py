import random

import py5

SIZE = 900


def setup():
    global photo
    py5.size(SIZE, SIZE)
    photo = py5.load_image("160.png")


def draw():
    py5.image(photo, 0, 0)
    py5.no_fill()
    py5.stroke_weight(50)
    py5.stroke(12, 75, 6)
    py5.rect(150, 150, 600, 600)
    py5.save_frame("concept.png")
    py5.no_loop()


py5.run_sketch()
