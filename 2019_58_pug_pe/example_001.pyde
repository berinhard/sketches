# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    size(1000, 600)
    stroke(color(27, 27, 27, 20))
    noFill()

x = 0
def draw():
    global x
    y = height / 2

    percent = x / float(width)
    percent = abs(0.5 - percent)
    h = lerp(0, 600, percent)
    w = lerp(600, 0, percent)
    ellipse(x, y, w, h)


    x += 5