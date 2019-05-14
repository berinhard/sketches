from pytop5js import *
from particles import Particle

max_particles = 200
particles = []

def setup():
    createCanvas(window.innerWidth, window.innerHeight)
    background(242)
    stroke(27)
    fill(242)

def draw():
    if len(particles) < max_particles:
        particles.append(Particle())

    to_remove = []
    for p in particles:
        if p.out_of_boundaries():
            to_remove.append(p)
        p.move()
        p.display()

    for p in to_remove:
        particles.remove(p)

# ==== This is required by pyp5js to work

# Register your events functions here
event_functions = {
}
start_p5(setup, draw, event_functions)
