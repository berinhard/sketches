# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches


def polygon(x, y, radius, num_points):
    """
    Python version of https://processing.org/examples/regularpolygon.html
    """
    angle = 0
    vertex_angle = TWO_PI / num_points
    
    points = []
    while angle < TWO_PI:
        sx = x + cos(angle) * radius
        sy = y + sin(angle) * radius
        points.append((sx, sy))
        angle += vertex_angle

    beginShape()
    for x, y in points:
        vertex(x, y)
    endShape(CLOSE)
    

class Hexagon:
    UP_NEIGHBOR = 0
    UR_NEIGHBOR = 1
    DR_NEIGHBOR = 2
    DW_NEIGHBOR = 3
    DL_NEIGHBOR = 4
    UL_NEIGHBOR = 5

    def __init__(self, location, radius):
        self.location = location
        self.radius = radius

    def display(self):
        polygon(self.location.x, self.location.y, self.radius, 6)

    def get_neighbor(self, index):
        # trigonometry
        angle = 180 + index * -60
        h = self.radius * sqrt(3)
        nx = self.location.x + sin(radians(angle)) * h
        ny = self.location.y + cos(radians(angle)) * h
        return Hexagon(PVector(nx, ny), self.radius)


class HexagonsLine:

    def __init__(self, start_location, radius, num_hexagons):
        current = Hexagon(start_location, radius)
        self.num_hexagons = num_hexagons
        self.hexagons = [current]
        for i in range(num_hexagons):
            if i % 2:
                next = current.get_neighbor(Hexagon.UR_NEIGHBOR)
            else:
                next = current.get_neighbor(Hexagon.DR_NEIGHBOR)
            self.hexagons.append(next)
            current = next

    def display(self):
        for hexagon in self.hexagons:
            hexagon.display()


class HexagonsGrid:

    def __init__(self, start_location, radius, num_lines, num_cols):
        self.lines = []
        line_location = start_location.copy()
        for i in range(num_lines):
            self.lines.append(HexagonsLine(line_location, radius, num_cols))
            line_location.y += radius * sqrt(3)

    def display(self):
        for i, hex_line in enumerate(self.lines):
            max_color = i * (255 // len(self.lines))
            red_color = map(noise(i + frameCount), 0, 1, 0, max_color)
            fill(red_color, 10, 47)
            hex_line.display()


def setup():
    background(0)
    size(700, 1000)
    noStroke()
    frameRate(10)

def draw():
    radius = 10
    num_lines = int(height / (2 * (radius * sqrt(3) / 2))) + 2
    num_cols = 5 * radius
    hex_grid = HexagonsGrid(PVector(-radius, -radius), radius, num_lines, num_cols)
    hex_grid.display() 
