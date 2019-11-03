# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


colors = [
    color(242, 242, 0, 1),
    color(242, 0, 242, 1),
    color(0, 242, 242, 1),
]


class Particula(object):

    def __init__(self):
        self.pos_x = width / 2
        self.pos_y = height / 2
        self.angulo = PI/4
        self.velocidade = 2
        self.cor = choice(colors)

    def atualiza(self):
        self.angulo += random(-0.5, 0.5)
        self.velocidade += random(-1, 1)

        self.pos_x += self.velocidade * cos(self.angulo)
        self.pos_y += self.velocidade * sin(self.angulo)

    def desenha(self, outra):
        strokeWeight(5)
        r, g, b = red(self.cor), blue(self.cor), green(self.cor)
        max_dist = sqrt(width ** 2 + height ** 2)
        a = map(
            dist(self.pos_x, self.pos_y, outra.pos_x, outra.pos_y), 0, max_dist, 10, 0
        )
        stroke(r, g, b, a)
        line(
            self.pos_x,
            self.pos_y,
            outra.pos_x,
            outra.pos_y
        )

num_particulas = 25
particulas = []

def setup():
    size(1200, 800)
    background(42)

    for i in range(num_particulas):
        particulas.append(Particula())


def draw():
    for p1, p2 in zip(particulas[::2], particulas[1::2]):
        p1.atualiza()
        p2.atualiza()
        p1.desenha(p2)


def keyPressed():
    if key == 's':
        saveFrame("cover.png")