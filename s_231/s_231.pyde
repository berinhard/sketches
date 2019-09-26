img = None

def setup():
    global img
    size(1280, 960)
    img = loadImage("img.jpg")

def draw():
    x = int(random(width))
    y = int(random(height))

    cor = img.get(x, y)
    r, g, b = red(cor), green(cor), blue(cor)

    if brightness(cor) > 120:  # 0 a 255
        fill(r, g, b)
    else:
        fill(r, 0, 0)
    noStroke()
    rect(x, y, 15, 15)


def keyPressed():
    if key == 's':
        saveFrame("cover.png")