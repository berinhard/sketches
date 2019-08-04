# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
# Example 001 for my tutorial at Python Nordeste 2019


def setup():
    size(900, 900)
    frameRate(2)
    background(120)
    strokeWeight(5)

x = 0
def draw():
    global x

    tamanho = 25
    linhas = range(0, height, tamanho)

    for y in linhas:
        stroke(random(255), random(255), random(255))
        if random(1) > 0.75:
            line(x, y, x + tamanho, y + tamanho)
        else:
            line(x, y + tamanho, x + tamanho, y)


    x += tamanho


def keyPressed():
    if key == 's':
        saveFrame("######.png")