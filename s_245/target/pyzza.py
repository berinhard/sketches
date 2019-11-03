from pyp5js import *
from random import choice


PEQUENA, MEDIA, GRANDE, MARACANA = 200, 300, 600, 900
NUM_FATIAS = [4, 8, 12, 16]


def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * cos(angle)
    y = y0 + r * sin(angle)

    return x, y


def area_pizza(tamanho):
    return PI * (tamanho / 2) ** 2


class Pizza():

    def __init__(self, tamanho):
        self.x, self.y = width / 2, height / 2
        self.tamanho = tamanho
        self.raio = tamanho / 2
        self.proporcao = area_pizza(self.tamanho) / area_pizza(GRANDE)

    def massa(self):
        fill(255, 199, 0)
        ellipse(width / 2, height / 2, self.tamanho, self.tamanho)

    def adiciona_ingrediente(self, ingrediente, quantidade):
        for i in range(int(quantidade * self.proporcao)):
            x = random(width)
            y = random(height)
            while dist(x, y, self.x, self.y) > (self.raio - 10):
                x = random(width)
                y = random(height)

            ingrediente(x, y)

    def fatiada(self, pedacos=8):
        noFill()
        stroke(27, 27, 27, 60)
        strokeWeight(2)
        angle_inc = TWO_PI / pedacos

        for i in range(1, pedacos + 1):
           arc(
                self.x,
                self.y,
                self.tamanho,
                self.tamanho,
                angle_inc * (i - 1),
                angle_inc * i,
                PIE
            )

    def borda_catupiry(self):
        strokeWeight(12 * self.proporcao)
        stroke(230)
        for i in range(360):
            angle = radians(i)
            r = self.raio + map(sin(i), -1, 1, -15, 5)
            x, y = polar_coordinate(self.x, self.y, r, angle)
            point(x, y)

    def borda_tradicional(self):
        noFill()
        strokeWeight(12 * self.proporcao)
        stroke(150, 100, 19)
        ellipse(self.x, self.y, self.tamanho, self.tamanho)


def muzzarella(x, y):
    noStroke()
    fill(255, 255, 0)
    rect(x, y, 5, 5)

def calabresa(x, y):
    noStroke()
    fill(255, 0, 0)
    ellipse(x, y, 30, 30)

def oregano(x, y):
    dir = p5.Vector.random2D()
    dir.mult(5)
    strokeWeight(1)
    stroke(2)
    line(x, y, x + dir.x, y + dir.y)

def alho(x, y):
    dir = p5.Vector.random2D()
    dir.mult(8)
    fill(27)
    triangle(x, y, x + dir.x, y, x, y + dir.y)

def azeitona(x, y):
    noFill()
    stroke(142, 0, 92)
    strokeWeight(5)
    ellipse(x, y, 20, 20)

def setup():
    createCanvas(950, 950)
    background(250)


def draw():
    pizza = Pizza(GRANDE)
    pizza.massa()
    pizza.adiciona_ingrediente(muzzarella, 5000)

    ingredientes_extras = [
        (calabresa, 100),
        (oregano, 2000),
        (alho, 1500),
        (azeitona, 50)
    ]
    for ingrediente, quantidade in ingredientes_extras:
        if random(1) > 0.5:
            pizza.adiciona_ingrediente(ingrediente, quantidade)

    pizza.fatiada(choice(NUM_FATIAS))

    if random(1) > 0.5:
        pizza.borda_tradicional()
    else:
        pizza.borda_catupiry()

    noLoop()
