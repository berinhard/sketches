# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

img = None
W, H = 1400, 1400
img_distr = []


possible_simetries = [
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
]
possible_offsets = [
    (0, 0, W/2, H/2),
    (W/2, 0, W, H/2),
    (0, H/2, W/2, H),
    (W/2, H/2, W, H),
]


def read_img_partial(range_offsets, simmetry):
    global img_distr

    x0, y0, x1, y1 = range_offsets
    symmetry_x, symmetry_y = simmetry
    new_distr = []
    for x in list(range(x0, x1))[::symmetry_x]:
        cols = []
        for y in list(range(y0, y1))[::symmetry_y]:
            cols.append(img.get(x, y))
        new_distr.append(cols)

    img_distr = new_distr


def img_symmetry(w, h, pattern):
    quadrants = [
        (0, 0, 1, 1),
        (w, 0, -1, 1),
        (0, h, 1, -1),
        (w, h, -1, -1),
    ]

    for x, y, off_x, off_y in quadrants:
        pushMatrix()
        translate(x, y)
        pattern(w, h, off_x, off_y)
        popMatrix()

def pattern(w, h, off_x, off_y):
    for x, line in enumerate(img_distr[::off_x]):
        for y, c in enumerate(line[::off_y]):
            pos = (x, y)
            pixel_x, pixel_y = screenX(*pos), screenY(*pos)
            set(pixel_x, pixel_y, c)

def setup():
    global img

    size(W, H)
    img = loadImage("113.png")
    img.resize(W, H)

def draw():
    counter = 1
    for offset in possible_offsets:
        for symmetry in possible_simetries:
            read_img_partial(offset, symmetry)
            img_symmetry(width / 2, height / 2, pattern)
            saveFrame("sample_{}.png".format(counter))
            counter += 1

    exit()
