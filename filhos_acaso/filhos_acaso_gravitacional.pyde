WIDTH, HEIGHT = 1400, 1400
px, py = 42, - HEIGHT / 2.1
start_angle = TWO_PI
angle = start_angle
CLOCK_FRAME_PACE = 500


def setup():
    size(WIDTH, HEIGHT)
    background(255)
    stroke(50, 50)
    strokeWeight(2)
    #blendMode(MULTIPLY)

    radius = range(width / 3, 0, -20)
    noStroke()
    for i, r in enumerate(radius):
        a = map(i, 0, len(radius), 0, 250 / 2)
        r = map(i, 0, len(radius), 170, 255)
        b = map(i, 0, len(radius), 210, 80)
        fill(r, b, 10, a)
        ellipse(width / 2, height / 2, r  , r )

    stroke(50, 50)

def draw():
    global px, py, angle

    pushMatrix()
    translate(width / 2, height / 2)

    if (not frameCount % CLOCK_FRAME_PACE):
        turn = frameCount / CLOCK_FRAME_PACE

        if turn < 10:
            stroke(50 + turn * 15, 50)
            angle = start_angle + turn * QUARTER_PI / 2
        elif turn == 10:
            #blendMode(BLEND)
            #stroke(124, 10, 2, 30)
            stroke(210, 80, 10, 30)
            angle = start_angle + turn * QUARTER_PI / 2
        elif turn > 12:
            saveFrame("####.png")
            noLoop()

    rotate(angle)
    margin_x = width / 7

    x = map(noise(frameCount * 0.006), 0, 1, px - margin_x, px + margin_x)
    y = map(noise(10 + frameCount * 0.008), 0, 1, py + 200, py + 550)

    line(px, py, x, y)
    popMatrix()

