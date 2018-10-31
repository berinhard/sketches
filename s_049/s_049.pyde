from random import choice

WHITE = color(235)  
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
GOLDEN = color(218, 145, 32)

CELL_SIZE = 50
CELL_SPACING = 0
ROW_SIZE = CELL_SIZE + CELL_SPACING
DIMENSION = 900
ORDER = (DIMENSION + ROW_SIZE) / ROW_SIZE
ARC_R = 100

GRID_RANGE = range(ORDER)

  
def setup():
    size(DIMENSION + ROW_SIZE + 10, DIMENSION + ROW_SIZE + 10)
    noStroke()
    strokeWeight(1)
    frameRate(1)


class RandomComposition():
    
    def __init__(self, i, j):
        self.i, self.j = i, j     
        d = CELL_SIZE   
        combinations = [        
            ((0, 0), (0, d), (d, d)),
            ((0, 0), (d, 0), (d, d)),
            ((0, d), (d, 0), (d, d)),
            ((0, d), (d, 0), (0, 0)),
        ]
        combinations_2 = [
            ((0, 0), (d/2, d/2), (d, 0)),
            ((0, 0), (d/2, d/2), (0, d)),            
            ((0, d), (d/2, d/2), (d, d)),
            ((d, d), (d/2, d/2), (d, 0)),
        ]
        self.value = choice(combinations_2)
        self.value_2 = choice([c for c in combinations_2 if not c == self.value])        
        
    def display(self):
        with pushMatrix():
            translate(self.i * ROW_SIZE, self.j * ROW_SIZE)
            prob = noise(self.i, self.j, frameCount / 10.0)
        
            fill(RED)
                                     
            p1, p2, p3 = self.value
            triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
            #p1, p2, p3 = self.value_2
            #triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
            
    
def save_video_frames(frame_rate, seconds, stop_run=True, extension="png", log_frame=True):
    num_frames = frame_rate * seconds
    
    if log_frame:
        print("{} /  {} - {}%".format(
            frameCount, int(num_frames), int(frameCount * 100 / num_frames)
        ))
    if frameCount <= num_frames:
        frame_name ="#" * (len(str(num_frames)))
        saveFrame("{}.{}".format(frame_name, extension))
    elif stop_run:
        noLoop()            
    
def draw():
    background(WHITE)
    translate(5, 5)
    d = CELL_SIZE

    for i in GRID_RANGE:
        for j in GRID_RANGE:
            composition = RandomComposition(i, j)
            composition.display()

                  
    save_video_frames(1.5, 10 * 60) 
    
def keyPressed():
    if key == 'n':
        redraw()
