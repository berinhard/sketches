# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    global move, target

    size(900, 900)
    move = PVector(random(900), random(900))

def draw():
    global move
    background(255)

    p1 = PVector(mouseX, mouseY)
    color_1 = color(255, 0, 0)

    p2 = move
    color_2 = color(255, 0, 255)

    dist = PVector.dist(p1, p2)
    c_percent = map(dist, 0, 900, 0, 1)
    moving_color = lerpColor(color_1, color_2, c_percent)


    fill(color_1)
    ellipse(p1.x, p1.y, 100, 100)
    fill(moving_color)
    ellipse(p2.x, p2.y, 100, 100)

    speed = 0.01
    move = PVector.lerp(p2, p1, speed)