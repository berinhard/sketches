from random import choice

WIDTH, HEIGHT = 1200, 700
current_height = HEIGHT - 100
current_width = 0
min_limit = 0 

PALETTE_1 = [
    (255,171,69),
    (129,138,141),
    (55,52,59),
    (127,124,85),
    (194,217,0),
]

PALETTE_2 = [
    (223,232,198),
    (208,216,182),
    (194,200,177),
    (185,188,174),
    (170,172,166),
    (140,132,162),
]

PALETTE_3 = [
(181,173,87),
(200,176,106),
(123,45,74),
(212,79,30),
(171,29,26),
(142,119,119)
]

def init_board():
    global limit_by_height

    limit_by_height = {
        HEIGHT: (0, WIDTH),
    }
    background(230, 230, 230)

def keyPressed():
    global COLORS, min_limit
    
    if key == '1':
        init_board()
        COLORS = PALETTE_1
    elif key == '2':
        init_board()
        COLORS = PALETTE_2
    elif key == '3':
        init_board()
        COLORS = PALETTE_3        

def setup():
    global WIDTH, HEIGHT, COLORS
    size(WIDTH, HEIGHT)
    frameRate(25)
    COLORS = PALETTE_2
    init_board()
        
def draw():
    global current_width, current_height, limit_by_height, min_limit
    if not limit_by_height:
        saveFrame("##########.png")
        init_board()

    current_height = max(limit_by_height)
    current_width, width_limit = limit_by_height[current_height]
          
    max_width = width_limit if width_limit > 10 else 200
    diff_width = map(noise(frameCount * 0.1) / 2, 0, 1, 0, max_width)
    if diff_width > width_limit - 10:
        diff_width = width_limit
                    
    x, y = current_width, current_height - map(random(1), 0, 1, 50, 200)
    w, h = diff_width, current_height - y
    
    c = sorted(COLORS)[frameCount % len(COLORS)]
    stroke(*c)
    fill(*c)
    rect(x, y, w, h)
    
    new_width, new_limit = current_width + diff_width, width_limit - diff_width
    if new_limit < 1:
        limit_by_height.pop(current_height)    
    else:
        limit_by_height[current_height] = (new_width, new_limit)
    
    if y >= 0:
        limit_by_height[y] = (x, w)
