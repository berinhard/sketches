# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/


class Particula(object):

    def __init__(self):
        self.pos_x = width / 2
        self.pos_y = height / 2
        self.angulo = PI/4
        self.velocidade = 2

    def atualiza(self):
        self.angulo += random(-0.5, 0.5)
        self.velocidade += random(-0.5, 0.5)

        self.pos_x += self.velocidade * cos(self.angulo)
        self.pos_y += self.velocidade * sin(self.angulo)

    def desenha(self):
        stroke(242)
        line(
            self.pos_x,
            self.pos_y,
            self.pos_x + self.velocidade * cos(self.angulo),
            self.pos_y + self.velocidade * sin(self.angulo),
        )

particulas = []

def setup():
    size(800, 600)

    for i in range(100):
        particulas.append(Particula())


def draw():
    fill(0, 3)
    noStroke()
    rect(0, 0, width, height)

    for particula in particulas:
        particula.atualiza()
        particula.desenha()


def keyPressed():
    if key == 's':
        save("cover.png")