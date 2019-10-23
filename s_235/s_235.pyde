# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
def setup():
    size(600, 600)
    background(255)

noise_x = 1
noise_x_inc = 0.012
noise_y = 1042
noise_y_inc = 0.024

def draw():
    global noise_x, noise_y

    offset = 100
    nx = noise(noise_x)
    x = map(nx, 0, 1, -offset, width + offset)
    ny = noise(noise_y)
    y = map(ny, 0, 1, -offset, height + offset)
    r = 30

    red_c = map(x, -offset, width + offset, 0, 255)
    green_c = map(y, -offset, height + offset, 0, 255)
    blue_c = 12
    transparencia = 1
    cor = color(red_c, green_c, blue_c, transparencia)
    stroke(cor)
    fill(cor)

    print(x)
    rect(x, y, r, r)

    noise_x += noise_x_inc
    noise_y += noise_y_inc


def keyPressed():
    if key == 's':
        saveFrame("cover.png")