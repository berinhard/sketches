import random

import py5

SIZE = 900
BACKGROUND = (255, 255, 255)


TARGET = py5.Py5Vector(0, 0)


def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * py5.cos(angle)
    y = y0 + r * py5.sin(angle)

    return py5.Py5Vector(x, y)


class Particle:

    def __init__(self, x=None, y=None):
        x = x if x else py5.width * 0.75
        y = y if y else py5.height / 4
        self.x, self.y = x, y
        self.location = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(0, 0)
        self.is_following = False
        self.top_speed = py5.random(5, 10)
        self.previous = None

    def move(self, target_pos=None):
        x, y = self.location.x, self.location.y
        self.previous = py5.Py5Vector(x, y )

        acc_t = py5.Py5Vector(target_pos.x, target_pos.y)
        acc_t.x =0
        acc_t.y = 0
        acc_t = TARGET
        acceleration = acc_t - self.location
        self.is_following = True

        acc_multiplier = py5.Py5Vector.random(dim=2)
        acc_multiplier *= py5.random(6)
        acceleration += acc_multiplier
        acceleration.normalize()
        acceleration *= 0.2


        self.velocity += acceleration
        self.velocity.set_limit(self.top_speed)
        self.location += self.velocity

    def draw(self):
        if not self.previous:
            return

        py5.stroke_weight(1)
        py5.stroke(42, 42, 42, 200)
        x, y = self.location.x, self.location.y
        py5.line(x, y, self.previous.x, self.previous.y)


PARTICLES = []
BOUNDARIES = []

def populate_particles(n=1000, r=300):
    for i in range(n):
        target = py5.Py5Vector(0, py5.random(py5.height / 2, py5.height))
        if py5.random() > 0.5:
            target = py5.Py5Vector(py5.random(0, py5.width / 2), py5.height)
        BOUNDARIES.append(target)

        angle = py5.random(0, py5.TWO_PI)
        l = r + py5.random(-30, 30)
        coord = polar_coordinate(py5.width / 2, py5.height / 2, l, angle)

        PARTICLES.append(Particle(coord.x, coord.y))


def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    py5.begin_record(py5.SVG, 'output.svg')
    py5.background(*BACKGROUND)
    populate_particles(1000)


def draw():
    for i, particle in enumerate(PARTICLES):
        target = BOUNDARIES[i]
        offset = 1
        if py5.random() >0.5:
            if target.x == 0:
                target.y -= offset
            else:
                target.x += offset

        target = py5.Py5Vector(py5.width / 2, py5.height / 2)
        if particle.location.dist(target) < 10:
            target = py5.Py5Vector(particle.x, particle.y)
        particle.move(target)
        particle.draw()

    if py5.is_key_pressed:
        if py5.key in ['s', 'S']:
            py5.end_record()
            py5.save_frame(f"{py5.frame_count}.png")
            py5.no_loop()

    print(py5.frame_count)


def mouse_clicked(e):
    global TARGET
    py5.println('mouse clicked:', e.get_action() == e.CLICK)
    TARGET = py5.Py5Vector(py5.mouse_x, py5.mouse_y)


py5.run_sketch()
