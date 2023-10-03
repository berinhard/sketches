import py5

from be5.coords import check_edges

SIZE = 900

particles = []


class Particle:

    def __init__(self, x=None, y=None):
        x = x if x else py5.random(py5.width)
        y = y if y else py5.random(py5.height)
        self.location = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(0, 0)
        self.is_following = False
        self.top_speed = 5

    def move(self, target_pos=None):
        if target_pos:
            acceleration = target_pos - self.location
            self.is_following = True

            acc_multiplier = py5.Py5Vector.random(dim=2)
            acc_multiplier *= 6
            acceleration += acc_multiplier
            acceleration.normalize()
            acceleration *= 0.2
        else:
            acceleration = py5.Py5Vector.random(dim=2)
            acceleration *= py5.random(1, 10) * 0.1
            self.top_speed = 7.5
        self.velocity += acceleration
        self.velocity.set_limit(self.top_speed)
        self.location += self.velocity


def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    py5.background(15)

    num_particles = 16
    particles.extend([
        Particle() for _ in range(num_particles)
    ])

noise_inc = 0

C_LINE = py5.color(240, 240, 240, 30)
C_FILL = py5.color(236, 71, 71)
C_FILL = py5.color(236,202,0)
C_FILL = py5.color(10,92,54)
#C_FILL = py5.color(236, 71, 71)
#C_FILL = py5.color(236, 71, 71)
#C_FILL = py5.color(236, 71, 71)


def draw():
    global noise_inc

    print(py5.frame_count)
    for i, particle in enumerate(particles[:2]):
        target_pos = None
        if i > 0:
            follows = particles[0]
            target_pos = follows.location

        particle.move(target_pos)
        if i > 0:
            noise_inc += 0.024
            noise_value = py5.noise(noise_inc)
            r = py5.remap(noise_value, 0, 1, 10, 60)

            #py5.stroke_weight(1)
            #py5.stroke(C_LINE)
            py5.no_stroke()
            py5.fill(C_FILL)
            x, y = particle.location.x, particle.location.y
            py5.circle(x, y, r)

        else:
            check_edges(particle.location)

    if py5.is_key_pressed:
        if py5.key in ['s', 'S']:
            py5.save_frame(f"{py5.frame_count}.png")


py5.run_sketch()
