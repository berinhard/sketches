#color http://palett.es/0088a0-6d8aff-ec63e5-fae2ce-6ce9c2
from random import choice
from custom_lines import CurveLine

def fibonacci_numbers(max_value):
    numbers = [0, 1]
    n1, n2 = 0, 1
    while n1 + n2 <= max_value:
        current = n1 + n2
        numbers.append(current)
        n1, n2 = n2, current
    return numbers

def setup():
    global stars
    
    size(1000, 600)
    background(0)
    frameRate(80)
    
    stars_coords = []
    for y in range(10, height / 2 - 10):
        stars_coords.append((choice(range(width)), y))
        
    stars = []
    for i in range(150):
        stars.append(choice(stars_coords))
    
def draw():
    global stars
    x_positions = fibonacci_numbers(width)
    noStroke()
    fill(0, 200)
    rect(0, 0, width, height / 2)
    fill(0, 10, 10, 200)
    rect(0, height / 2 - 5, width, height)
        
    sea_lines = []
    for i ,y in enumerate(range(height / 2, height, 10)):
        t = float(frameCount) / 100 + float(i) / 10
        y = y + map(noise(t), 0, 1, -5, 5)
        sea_lines.append((0, y, width, y))
    
    wave_colors = [
        (0, 136, 160, 60), # GREEN
        (0, 136, 160, 60),
        (9, 138, 255, 60), # BLUE
        (9, 138, 255, 60),
        (9, 138, 255, 60),
    ]
    strokeWeight(3)
    for i, wave in enumerate(sea_lines):
        sx, sy, ex, ey = wave
        curve_line = CurveLine((sx, sy), (ex, ey))
        curve_line.display(width / 100, choice(wave_colors))
      
    stroke(250, 226, 206, 130)
    for star in stars:
        strokeWeight(map(noise(star[0] + frameCount), 0, 1, 1, 5))
        point(*star)
        
    noStroke()
    fill(250, 226, 206, 240)
    ellipse(width - 100, 80, 60, 60)
    
    # glitch lines
    stroke(236,99,229, 100)
    strokeWeight(2)
    for i, x in enumerate(x_positions[1:]):
        x_diff = x - x_positions[i]
        x = map(noise(x + frameCount * 0.1), 0, 1, x-x_diff, x+x_diff)
        if random(0, 1) > 0.80:
            line(x, 0, x, height)
