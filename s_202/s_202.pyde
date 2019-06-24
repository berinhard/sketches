# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


d = 10
from_center = 200


class Fragment:

    def __init__(self):
        self.pos = PVector(width / 2, height / 2)
        self.direction = PVector.random2D()
        self.direction.mult(0.5)
        self._stop = False

    @property
    def hit_bottom(self):
        return self._stop

    def dist(self, fragment):
        dx = fragment.pos.x - self.pos.x
        dy = fragment.pos.y - self.pos.y
        return dx * dx + dy * dy

    def move(self):
        self.pos.add(self.direction)

    def stuck_to(self, bottom):
        if not self.hit_bottom:
            self.move()

            if self.pos.dist(PVector(width/2, height/2)) >= from_center:
                self._stop = True
                return

            for b in bottom:
                distance = self.dist(b)
                if distance <= d * (d / 2):
                    self._stop = True
                    break

    def display(self):
        c = map(self.pos.dist(PVector(width/2, height/2)), 0, from_center, 0, 255)
        fill(color(c, 137, 255))
        noStroke()
        ellipse(self.pos.x, self.pos.y, d, d)


fragments = []
bottom = []


def setup():
    size(700, 500)
    colorMode(HSB)


def draw():
    background(27)
    fragment = Fragment()

    if len(fragments) < 1000:
        fragments.append(fragment)

    finished = [f for f in fragments if f.hit_bottom]
    for f in finished:
        bottom.insert(0, f)
        fragments.remove(f)

    for fragment in fragments:
        fragment.stuck_to(bottom)

    for f in bottom:
        f.display()


def keyPressed():
    if key == 's':
        saveFrame("###########.png")