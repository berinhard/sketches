# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    size(900, 600)
    noFill()
    background(27)
    strokeWeight(7)

x = 0
def draw():
    global x
    y = height / 2

    stroke(240, 240, 240, 6)
    percent = x / float(width)
    percent = abs(0.5 - percent)
    h = lerp(0, 600, percent)
    w = lerp(600, 0, percent)
    with pushMatrix():
        translate(x, y)
        rotate(radians(frameCount))
        ellipse(0, 0, w, h)

    stroke(212, 28, 42, 10)
    percent = x / float(width)
    percent = abs(0.5 - percent)
    h = lerp(600, 0, percent)
    w = lerp(0, 600, percent)
    with pushMatrix():
        translate(x, y)
        rotate(radians(frameCount))
        ellipse(0, 0, w, h)

    x += 5

def keyPressed():
    if key == 's':
        saveFrame("####.png")