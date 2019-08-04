# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
# Example 003 for my tutorial at Python Nordeste 2019


from random import choice

colors = [
    color(0, 153, 204),
    color(  204, 255, 204 ),
    color( 102, 204, 255 ),
    color( 0, 51, 153 ),
]

class Particle(object):

    def __init__(self):
        self.x = random(width)
        self.y = random(height)
        self.tamanho = 50
        self.color = choice(colors)

    def atualiza(self):
        self.x += random(-3, 3)
        self.y += random(-3, 3)

        self.tamanho -= 1

    def desenha(self):
        if self.tamanho < 0:
            return
        stroke(27, 27, 27, 90)
        fill(self.color)
        ellipse(self.x, self.y, self.tamanho, self.tamanho)

particles = []
num_particles = 300

def setup():
    global particle

    size(800, 800)
    background(250)
    for i in range(num_particles):
        particle = Particle()
        particles.append(particle)

def draw():
    for particle in particles:
        particle.atualiza()
        particle.desenha()

def keyPressed():
    if key == 's':
        saveFrame("###########.png")
