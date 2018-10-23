from random import choice

WHITE = color(235)
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)

def setup():
    size(1600, 800)
    background(WHITE)
    strokeWeight(1.5)
    textAlign(CENTER)


def get_fibonacci_numbers(num_numbers):
    numbers = []
    for i in range(num_numbers):
        try:
            number = numbers[i - 1] + numbers[i - 2]
        except IndexError:
            number = 1
        numbers.append(number)
    return numbers


def draw():
    global x
    fill(BLACK)
    total_points = 50000

    num_cols = 10
    powers = get_fibonacci_numbers(15)
    spacing = 2
    col_width = width / num_cols

    for counter in range(num_cols):
        x_offset = col_width * counter
        col_x_range = [x_offset + spacing, x_offset + (col_width - 2 * spacing)]
        power = powers[counter]

        #fill(BLACK)
        #text("{}".format(power), x_offset + col_width / 2, 720)
        for i in range(total_points):
            x = random(*col_x_range)
            y = random(1)
            y = 100 + y ** power * 600
            stroke(BLACK)
            point(x, y)

            x = random(*col_x_range)
            y = random(1)
            y = (height - 100) - y ** power * 600
            #y = height - y
            stroke(RED)
            point(x, y)

    #saveFrame("teste_y_espelhado.png")
    noLoop()



