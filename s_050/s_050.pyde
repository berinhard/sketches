IMAGES_OFFSET = 80
WIDTH = 1000
HEIGHT = 1000
IMG_HEIGHT = 100
NUM_COLS = HEIGHT / IMG_HEIGHT
WHITE = color(235)
WHITE_LINE = color(185)  
RED = color(171, 12, 10)
BLACK = color(17, 17, 17) 
 
def setup():
    size(WIDTH, HEIGHT)
    #frameRate(1)
    
    
def save_video_frames(frame_rate, seconds, stop_run=True, extension="png", log_frame=True):
    """
    # https://gist.github.com/berinhard/d2ef20f361f70b7c0a216957d993efb2
    Save the required number of frames given for `seconds` with the given `frame_rate`.
    
    stop_run: calls noLoop() after saving all frames
    extension: file extension
    log_frame: enables logging in the terminal
    """
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
    background(BLACK)
    
    n_start = random(100000)
    rects_widths = [ 
        random(1) for i in range(208)
    ]
    rects_widths = [map(w, 0, 1, 60, 120) for w in rects_widths ]
    
    points = []
    for j in range(NUM_COLS + 1):
        y = j * IMG_HEIGHT
        line_width = 0
        while rects_widths:
            rect_width = rects_widths[0]
            if line_width + rect_width > WIDTH + 2 * IMAGES_OFFSET:
                break
            
            fill(WHITE)
            stroke(WHITE_LINE)
            if random(1) ** 3 > 0.92:
                fill(BLACK)
                stroke(BLACK)
            rect(line_width, y, rect_width, IMG_HEIGHT)
            if random(1) > 0.87:
                x, y = line_width + rect_width / 2, y + IMG_HEIGHT / 2
                if 0 < x < width and 0 < y < height:
                    points.append((line_width + rect_width / 2, y + IMG_HEIGHT / 2))            
                        
            if not line_width:
                line_width += rect_width / 2
            else:
                line_width += rect_width
            rects_widths.pop(0)
            
    noStroke()
    fill(RED)
    beginShape()
    for x, y in points:
        curveVertex(x, y)
    endShape(CLOSE)
    
    #save_video_frames(0.5, 60 * 10)
                
        
    
    
    
