# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.save_frames import save_video_frames

WHITE = color(230, 230, 230)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)


def setup():
    size(870, 800)
    background(BLACK)
    strokeWeight(4)
    noFill()


STEPS = 10
lower_points, upper_points = [], []
current_step = STEPS
upper_noise_t, lower_noise_t = 0, 1042

def draw():
    global upper_noise_t, current_step, lower_points, upper_points, lower_noise_t

    background(BLACK)
    angle = 0
    inc = TWO_PI / 25.0
    y0 = height / 2

    if current_step == STEPS:
        upper_noise_t += 1
     #   if random(1) > 0.73:
        angle = map(noise(upper_noise_t), 0, 1, 0, PI)
        y_diff = sin(angle) * map(noise(upper_noise_t), 0, 1, 50, 500)
        lower_points.append((0, y0 + y_diff))

        lower_noise_t += 0.72
     #   if random(1) > 0.73:
        angle = map(noise(lower_noise_t), 0, 1, PI, TWO_PI)
        y_diff = sin(angle) * map(noise(lower_noise_t), 0, 1, 50, 500)
        upper_points.append((width, y0 + y_diff))

    stroke(WHITE)
    walk = 1
    for i, coords in enumerate(lower_points):
        x, y = coords
        line(x, y0 + 2, x, y)
        lower_points[i] = (x + walk, y)

    stroke(RED)
    for i, coords in enumerate(upper_points):
        x, y = coords
        line(x, y0 - 2, x, y)
        upper_points[i] = (x - walk, y)

    current_step -= 1
    if current_step < 0:
        current_step = STEPS

    lower_points = [(x, y) for x, y in lower_points if not x > width]
    upper_points = [(x, y) for x, y in upper_points if x > 0]

    save_video_frames(60, 60)