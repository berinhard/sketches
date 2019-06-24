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


class Fragment:

    def __init__(self, x, y=0):
        self.pos = PVector(x, y)
        self._stop = False

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    @x.setter
    def x(self, value):
        self.pos.x = constrain(int(value), 0, width)

    @y.setter
    def y(self, value):
        self.pos.y = constrain(int(value), 0, height)

    @property
    def hit_bottom(self):
        return self._stop

    def dist(self, fragment):
        dx = fragment.pos.x - self.pos.x
        dy = fragment.pos.y - self.pos.y
        return dx * dx + dy * dy

    def fall(self, bottom):
        if not self.hit_bottom:
            self.pos.add(PVector(random(-2, 2), random(2)))

            if self.pos.y >= height:
                self._stop = True

            for b in bottom:
                distance = self.dist(b)
                if distance <= d * (d / 2):
                    self._stop = True
                    break

    def display(self):
        noStroke()
        c = map(self.y, height, 0, 0, 255)
        fill(color(c, 137, 255))
        ellipse(self.x, self.y, d, d)


fragments = []
bottom = []


def setup():
    size(900, 400)
    colorMode(HSB)


def draw():
    background(27)
    fragment = Fragment(random(width))

    if len(fragments) < 1000:
        fragments.append(fragment)

    for i in range(500):
        finished = [f for f in fragments if f.hit_bottom]
        for f in finished:
            bottom.insert(0, f)
            fragments.remove(f)

        for fragment in fragments:
            fragment.fall(bottom)

    for f in bottom:
        f.display()




def keyPressed():
    if key == 's':
        saveFrame("###########.png")