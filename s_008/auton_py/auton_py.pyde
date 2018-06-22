"""
Adaptado de @villares: https://github.com/arteprog/quatro-encontros/blob/master/gameOfLife01_py/gameOfLife01_py.pyde
Adaptado de The Nature of Code, Daniel Shiffman http://natureofcode.com
"""

CELL_SIZE = 4

def init():
    """ fill board with random values 0 or 1 """
    for i in range(COLS):
        for j in range(ROWS):
            BOARD[i][j] = int(random(2))

def setup():
    global COLS, ROWS, BOARD, quadrant_times
    # initialize noise time for each quadrant
    quadrant_times = [0, 0.3, 0.6, 0.9]
    
    size(600, 400)
    # Initialize ROWS, COLS and set-up arrays
    COLS = width / CELL_SIZE
    ROWS = height / CELL_SIZE
    # Game of life BOARD
    BOARD = [[0] * ROWS for _ in range(COLS)]
    # Call function to fill board with random values 0 or 1
    init()
    background(0);

def get_quadrand_point(q_index):
    "Given the quadrant index, return the x, y coordinates for its point"
    global quadrant_times
    
    x = width / 2 * noise(quadrant_times[q_index])
    y = height / 4  * noise(quadrant_times[q_index - 2])
    if q_index in [2, 3]:
        y += height / 2
        
    if q_index in [1, 3]:
        x += width / 2
        
    return x, y

def draw():
    global quadrant_times
    
    fill(0, 35)
    stroke(0)
    rect(0, 0, width, height)
    px, py = width / 2, 0
    for j in range(ROWS):
        for i in range(COLS):
            if not BOARD[i][j]:
                continue
         
            x, y = i * CELL_SIZE, j * CELL_SIZE            
            quadrant_index = 0 
            if x > width / 2:
                quadrant_index += 1
            if y > height / 2:
                quadrant_index += 2
        
            qx, qy = get_quadrand_point(quadrant_index)
            if frameCount > 10:
                stroke((255 + x * y) % 255, 180, 0, 90)
                line(qx, qy, x, y)  # line from previous cell to current
                line(px, py, x, y)  # line from quadrant position to current          
            px, py = x, y 

    generate()
        
    quadrant_times[0] += 0.01
    quadrant_times[1] += 0.035
    quadrant_times[2] += 0.035
    quadrant_times[3] += 0.01


def generate():
    """ The process of creating the new generation """
    global BOARD
    next = [[0] * ROWS for _ in range(COLS)]
    # Loop through every spot in our 2D array and check spots neighbors
    for y in range(ROWS):
        for x in range(COLS):
            # Add up all the states in a 3x3 surrounding grid
            neighbors = 0
            for i in range(-2, 3):
                for j in range(0, 2):
                    nx = (x + i + COLS) % COLS
                    ny = (y + j + ROWS) % ROWS
                    neighbors += BOARD[nx][ny]
            # A little trick to subtract the current cell's state since
            # we added it in the above loop
            neighbors -= BOARD[x][y]
            # Rules of Life
            if   BOARD[x][y] == 1 and neighbors < 3 : next[x][y] = 0 # Loneliness
            elif BOARD[x][y] == 1 and neighbors > 4 : next[x][y] = 0 # Overpopulation
            elif BOARD[x][y] == 0 and neighbors == 4: next[x][y] = 1 # Reproduction
            else:                                     next[x][y] = BOARD[x][y]  # Stasis
    # Next is now our board
    BOARD = next
