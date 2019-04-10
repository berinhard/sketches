# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    global move, target

    size(900, 900)
    move = random(900), random(900)
    target = random(900), random(900)

def draw():
    global move
    background(255)

    fill(255, 0, 0)
    x1, y1 = mouseX, mouseY
    ellipse(x1, y1, 100, 100)

    fill(255, 0, 255)
    x2, y2 = move
    ellipse(x2, y2, 100, 100)

    speed = 0.01
    x = lerp(x2, x1, speed)
    y = lerp(y2, y1, speed)
    move = (x, y)