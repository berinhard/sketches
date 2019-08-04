# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
# Example 002 for my tutorial at Python Nordeste 2019

x = 0
y = 0
px = 0
py = 0

def keyPressed():
    if key == 's':
        saveFrame("###########.png")

def setup():
    global px, py
    size(900, 900)
    strokeWeight(2)
    stroke(27)
    background(245)

    step_x = 0 * 0.012
    step_y = (0 + 1042368) * 0.07

    px = noise(step_x) * height
    py = noise(step_y) * width

def draw():
    global x, y, px, py

    step_x = frameCount * 0.012
    step_y = (frameCount + 1042368) * 0.07

    x = noise(step_x) * height
    y = noise(step_y) * width

    line(px, py, x, y)
    px, py = x, y
