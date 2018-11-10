def setup():
    global px, py

    size(800, 800)
    background(255)
    strokeWeight(4)
    colorMode(HSB, 100)
    rectMode(CENTER)

    px = noise(0) * width
    py = noise(1042 / 138.0) * height

def draw():
    global px, py

    x = noise(frameCount / 97.0) * (width + 100)
    y = noise((frameCount + 1042) / 138.0) * (height + 100)
    color_position = map(y, 0, height, 0, 100)

    stroke(color(color_position, 80, 80))
    line(px, py, x, y)
    px, py = x, y
    if random(1) > 0.97:
        rect(x, y, 40, 40)

def keyPressed():
    if key == 's':
        saveFrame("#######.png")