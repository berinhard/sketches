# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import draw_shape
from berin.save_frames import save_video_frames


WHITE = color(228, 228, 228, 200)
BLACK = color(27, 27, 27)

LINE_STEP = 10
MAX_VARIANCE = 200

def setup():
    size(502, 902)
    strokeWeight(2)
    stroke(WHITE)
    noFill()
    #frameRate(12)

def draw():
    background(BLACK)
    for j, y in enumerate(range(0, height + 100, LINE_STEP)):
        new_line = []
        line_center = PVector(width / 2, y)

        for i, x in enumerate(range(0, width, 20)):
            noise_steps = [
                i * 0.8,
                (j + frameCount) * 0.1
            ]
            n = noise(*noise_steps)

            dist_to_center = line_center.dist(PVector(x, y))
            variance = max(MAX_VARIANCE - dist_to_center, 0) / 100

            x_y = y + map(n, 0, 1, -80, 0) * variance

            new_line.append(PVector(x, x_y))

        draw_shape(new_line)


    save_video_frames(12, 60)