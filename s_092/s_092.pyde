# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.save_frames import save_video_frames


GREEN = color(49, 114, 59)
WHITE = color(198)
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
GOLDEN = color(218, 145, 32)


class SymmetricArcs():

    def __init__(self, x, y, start_angle, noise_step=0.1, noise_start=0, arc_angle=QUARTER_PI, color=WHITE):
        self.x, self.y = x, y
        self.color = color
        self.start_angle = start_angle
        self.arc_angle = arc_angle
        self.noise_pos = noise_start
        self.noise_step = noise_step
        self.r = 850 * noise(self.noise_pos)

    def update(self):
        self.noise_pos += self.noise_step
        self.r = 850 * noise(self.noise_pos)

    def draw(self):
        angle_1 = self.start_angle
        angle_2 = self.start_angle + PI
        fill(self.color)
        arc(0, 0, self.r, self.r, angle_1, angle_1 + self.arc_angle, PIE)
        arc(0, 0, self.r, self.r, angle_2, angle_2 + self.arc_angle, PIE)


SYM_ARCS = [
    SymmetricArcs(0, 0, 0, noise_step=0.025, color=RED),
    SymmetricArcs(0, 0, QUARTER_PI, noise_step=0.002,  color=GREEN),
    SymmetricArcs(0, 0, HALF_PI, noise_step=0.018,  color=GOLDEN),
    SymmetricArcs(0, 0, 3 * QUARTER_PI, noise_step=0.02,  color=BLACK),
]


def setup():
    noStroke()
    size(850, 850)
    strokeWeight(1)
    frameRate(24)


def draw():
    background(WHITE)
    with pushMatrix():
        translate(width / 2, height / 2)
        rotate(radians(frameCount))
        for sym_arcs in SYM_ARCS:
            sym_arcs.update()
            sym_arcs.draw()

    save_video_frames(24, 60)