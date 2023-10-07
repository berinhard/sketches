import py5

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

    def draw(self):
        if self.is_following:
            py5.stroke_weight(4.6)
            py5.stroke(0, 168, 42, 100)
        else:
            py5.stroke_weight(6.4)
            py5.stroke(235, 71, 71, 200)
        x, y = self.location.x, self.location.y
        py5.point(x, y)
        print(x, y)

