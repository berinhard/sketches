import os
from random import shuffle

IMAGES_OFFSET = 4
WIDTH = 1000
HEIGHT = 1000
IMG_HEIGHT = 80
NUM_LINES = HEIGHT / IMG_HEIGHT
WHITE = color(235)
WHITE_LINE = color(185)
RED = color(218, 12, 10)
BLACK = color(17, 17, 17)

generals = []
generals_right_position = []
people = []

def settings():
    people_images = os.listdir('/home/bernardo/workspace/sketches/s_051/data/')
    generals_images = os.listdir(
        '/home/bernardo/workspace/sketches/s_051/data/generais/')

    for filename in people_images:
        if not filename.endswith(".jpg"):
            continue
        print(filename)
        img = loadImage(filename)
        while not img:
            pass
        img.resize(0, IMG_HEIGHT)
        img.filter(GRAY)
        people.append(img)

    
    for filename in ['generais/' + f for f in generals_images]:
        print(filename)
        img = loadImage(filename)
        while not img:
            pass
        img.resize(0, IMG_HEIGHT)
        generals.append(img)
        if filename.startswith('generais/head'):
            generals_right_position.append(img)

def setup():
    size(WIDTH, HEIGHT + 5)    
    font = createFont("NeutralStd-Bold.otf", 50)
    textAlign(CENTER)
    rectMode(CENTER)
    textFont(font)
    frameRate(0.75)


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
        frame_name = "#" * (len(str(num_frames)))
        saveFrame("{}.{}".format(frame_name, extension))
    elif stop_run:
        noLoop()
        
def display_all_people(heads):
    points = []
    for j in range(NUM_LINES + 1):
        y = j * (IMG_HEIGHT + IMAGES_OFFSET)
        line_width = -50
        while heads:
            img_width = heads[0].width
            if line_width + img_width > WIDTH + 100:
                break
            img = heads.pop(0)

            if img in generals:
                tint(RED)
            else:
                tint(210)
            image(img, line_width, y)
            line_width += img_width + IMAGES_OFFSET
            
def display_generals_questions():
    label_line = NUM_LINES / 2
    #y = label_line * (IMG_HEIGHT + IMAGES_OFFSET) - IMG_HEIGHT / 2
    y = height / 2
    
    fill(BLACK)
    stroke(BLACK)
    rect(width / 2, height / 2, width, IMG_HEIGHT)
    fill(WHITE)
    text("quem tem medo do general?", width / 2, y + 15)
    
general_frames = 0

def draw():
    global general_frames
    
    background(BLACK)
    
    if general_frames:
        heads = []
        for i in range(20):
            heads += generals[:]
    else:
        heads = people + generals_right_position
        
    shuffle(heads)      
    display_all_people(heads)
    if general_frames:
        display_generals_questions()
        general_frames -= 1
    
    prob = random(1)
    if prob > 0.85 and not general_frames:
        general_frames = int(random(1, 5))
    
    #noLoop()
    #save_video_frames(0.75, 60 * 10)
