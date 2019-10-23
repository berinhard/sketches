# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
class Particula(object):

    def __init__(self):
        self.x = random(width)
        self.y = random(height)
        self.raio = random(50, 100)
        self.angulo = random(TWO_PI)
        self.angulo_inc = random(TWO_PI / 36)
        self.raio_inc = random(3, 9)

    def atualize(self):
        self.color = color(210, random(0, 200), 87)
        self.raio -= self.raio_inc
        self.angulo += self.angulo_inc

    def desenha(self):
        if self.raio > 0:
            with pushMatrix():
                translate(self.x, self.y)
                rotate(self.angulo)
                fill(self.color)
                rect(0, 0, self.raio, self.raio)

num_particulas = 1000
particulas = []
def setup():
    size(600, 600)
    rectMode(CENTER)

    for i in range(num_particulas):
        particula = Particula()
        particulas.append(particula)

def draw():
    for particula in particulas:
        particula.atualize()
        particula.desenha()


def keyPressed():
    if key == 's':
        saveFrame("cover.png")