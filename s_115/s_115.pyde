# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

BLACK = color(27)
WHITE = color(235, 235, 235, 30)
RED = color(181, 32, 10, 30)
BLUE = color(55,189,182, 30)
YELLOW = color(255, 255, 0, 30)
MAGENTA = color(255, 0, 255, 30)

current_noise_step_x = random(10000)
noise_inc_x = 0.013
current_noise_step_y = random(10000)
noise_inc_y = 0.0887

second_current_noise_step_x = random(10000)
second_noise_inc_x = 0.01
second_current_noise_step_y = random(10000)
second_noise_inc_y = 0.0098

def setup():
    size(900, 900)
    background(BLACK)
    stroke(WHITE)
    strokeWeight(2)

def draw():
    global current_noise_step_x, current_noise_step_y
    global second_current_noise_step_x, second_current_noise_step_y

    x1 = noise(current_noise_step_x) * (width + 100)
    y1 = noise(current_noise_step_y) * height / 2

    current_noise_step_x += noise_inc_x
    current_noise_step_y += noise_inc_y

    x2 = noise(second_current_noise_step_x) * (width + 100)
    y2 = noise(second_current_noise_step_y) * height / 2  + height / 2

    second_current_noise_step_x += second_noise_inc_x
    second_current_noise_step_y += second_noise_inc_y

    mid_x = lerp(x1, x2, 0.5)
    mid_y = height / 2 + map(noise(frameCount), 0, 1, -30, 30)
    stroke(WHITE)
    line(x1, y1, mid_x, mid_y)
    stroke(YELLOW)
    line(mid_x, mid_y, x2, y2)


    if frameCount == 1000:
        saveFrame("######.png")
        noLoop()
    print(frameCount)

def keyPressed():
    if key == 's':
        saveFrame("#######.png")