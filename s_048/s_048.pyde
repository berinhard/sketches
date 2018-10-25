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
    frameRate(1.5)

    
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
    background(RED)
    translate(5, 5)
    d = CELL_SIZE
    triangles_comb = [
        (0, 0, 0, d, d, d),
        (0, 0, d, 0, d, d),
        (0, d, d, 0, d, d),
        (0, d, d, 0, 0, 0),
    ]
                
    for i in GRID_RANGE:
        for j in GRID_RANGE:
            with pushMatrix():
                translate(i * ROW_SIZE, j * ROW_SIZE)
                prob = noise(i, j, frameCount / 10.0)
                
                x1, y1, x2, y2, x3, y3 = choice(triangles_comb)
                #index = int(map(prob, 0, 1, 0, 360) / 90)
                #x, y, angle_start, angle_end = arcs_comb[index]
                 
                if prob > 0.32:
                    fill(BLACK)
                else:
                    fill(GOLDEN)      
                            
                triangle(x1, y1, x2, y2, x3, y3)
                  
    #save_video_frames(1.5, 10 * 60) 
    
def keyPressed():
    if key == 'n':
        redraw()
