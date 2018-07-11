import math
from random import choice

from continuous_line import ContinuousLine


def hilbert(points, x0, y0, xi, xj, yi, yj, n):
    """
    From here: http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
    """
    if not n:
        line_x = x0 + (xi + yi) / 2
        line_y = y0 + (xj + yj) / 2
        points.append((line_x, line_y))
    else:
        n -= 1
        hilbert(points, x0, y0, yi / 2, yj / 2, xi / 2, xj / 2, n),
        hilbert(points, x0 + xi / 2, y0 + xj / 2,
                xi / 2, xj / 2, yi / 2, yj / 2, n),
        hilbert(points, x0 + xi / 2 + yi / 2, y0 + xj / 2 + yj / 2,
                xi / 2, xj / 2, yi / 2, yj / 2, n),
        hilbert(points, x0 + xi / 2 + yi, y0 + xj / 2 +
                yj, -yi / 2, -yj / 2, -xi / 2, -xj / 2, n),

COLORS = [
    "#1450CC",
    "#1450CC",
    "#1450CC",
    "#1450CC",
    "#405D99",
    "#405D99",
    "#405D99",
    "#00D9FF",
    "#00D9FF",
    "#FF7A40",
    "#FF7A40",
    "#CC3214",
]

def setup():
    size(1000, 1000)
    background(0)
    strokeWeight(2.5)
    strokeCap(ROUND)
    global points_4, points_5, points_6, points_7, live_lines
    frameRate(8)

    points_4, points_5, points_6, points_7, live_lines = [], [], [], [], []
    hilbert(points_4, 0, 0, width, 0, 0, height, 4)
    hilbert(points_5, 0, 0, width, 0, 0, height, 5)
    hilbert(points_6, 0, 0, width, 0, 0, height, 6)
    hilbert(points_7, 0, 0, width, 0, 0, height, 7)

def draw():
    global points_4, points_5, points_6, points_7, live_lines

    noStroke()
    fill(0, 200)
    rect(0, 0, width, height)
    
    if frameCount % 5:
        points = choice([points_4, points_5, points_6, points_7])
        print(len(live_lines))
        if len(live_lines) > 200:
            live_lines = []
            direction *= -1
        colors = choice(COLORS)
        live_lines.append(ContinuousLine(points, colors=colors))

    noStroke()
    for c_line in live_lines[:]:
        if c_line.is_dead:
            live_lines.remove(c_line)
        else:
            c_line.display()

    saveFrame("path-{}.jpg".format(frameCount))
