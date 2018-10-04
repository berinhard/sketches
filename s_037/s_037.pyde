# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Adapted fro Alexandre B A Villares' grid function
# Source: http://abav.lugaralgum.com/sketch-a-day/

# Cool bug found while studying the code
from lines import LinesPositioning, BLACK, WHITE


class GridControl():

    def __init__(self, x, y, order, spacing, cell_width=100, cell_height=100):
        self.x, self.y = x, y
        self.order, self.spacing = order, spacing
        self.cell_width, self.cell_height = cell_width, cell_height
        self.reset()

    def reset(self):
        self.callables_grid = [[[] for j in range(self.order)] for i in range(self.order)]

    def register_functions_per_cell(self, factory, *args, **kwargs):
        for i in range(self.order):
            gx = i * self.spacing
            for j in range(self.order):
                gy = j * self.spacing
                self.callables_grid[i][j].extend(factory(gx, gy, self.cell_width, self.cell_height, *args, **kwargs))

    def display(self):
        with pushMatrix():
            translate(self.x, self.y)
            for i in range(self.order):
                gx = i * self.spacing
                for j in range(self.order):
                    gy = j * self.spacing
                    for function, args, kwargs in self.callables_grid[i][j]:
                        function(gx, gy, *args, **kwargs)


custom_grid = GridControl(25, 12.5, 10, 100)


def cell_border(gx, gy, cell_width, cell_height):
    strokeWeight(1)
    stroke(BLACK)
    rect(gx, gy, cell_width, cell_height)


def per_cell_function_factory(gx, gy, cell_width, cell_height):
    max_lines = int(map(random(1), 0, 1, 10, 80))
    positions = LinesPositioning(
        gx,
        gy,
        max_width=gx + cell_width,
        max_height=gy + cell_height,
        max_lines=max_lines)

    return [
        (positions.new_random_line_and_display, (), {}),
        (positions.refresh, (), {}),
        #(cell_border, (cell_width, cell_height), {}),
    ]

def setup():
    noFill()
    size(1050, 1050)
    frameRate(10)
    strokeWeight(2)
    custom_grid.register_functions_per_cell(per_cell_function_factory)

def draw():
    background(WHITE)
    custom_grid.display()

    if not frameCount % 333:
        custom_grid.reset()
        custom_grid.register_functions_per_cell(per_cell_function_factory)
    print(frameCount)

    # if frameCount >= 6000:
    #     noLoop()
    # saveFrame("####.png")


def keyPressed():
    if key == " ":
        custom_grid.reset()
        custom_grid.register_functions_per_cell(per_cell_function_factory)
        redraw()

