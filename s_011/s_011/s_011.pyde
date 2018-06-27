from random import choice

GRID_SIZE = 40
SKETCH_NAME = "s177"
OUTPUT = ".gif"

class Cell(object):

    def __init__(self, x, y, border, spacing, line_color=None):
        self.index_x, self.index_y = x, y
        self.border = border
        self.spacing = spacing
        self._line_color = line_color

    @property
    def x(self):
        return self.border + self.spacing / 2 + self.index_x * self.spacing

    @property
    def y(self):
        return self.border + self.spacing / 2 + self.index_y * self.spacing
    
    @property
    def line_color(self):
        if not self._line_color:
            self._line_color = choice([
                "#005365",
                "#44929f",
                "#ddc963",
                "#c29400",
            ])
        return self._line_color

    def link(self, cell):
        stroke(self.line_color)
        line(self.x, self.y, cell.x, cell.y)

    def __eq__(self, cell):
        return self.x == cell.x and self.y == cell.y

    def neighbors(self, grid_size):
        x_range = [0, 1]
        y_range = [0, 1]

        if 0 < self.index_x < grid_size:
            x_range.append(-1)
        if 0 < self.index_y < grid_size:
            y_range.append(-1)

        for x in x_range:
            for y in y_range:
                if abs(x - y) != 2:
                    continue
                neigh = Cell(self.index_x + x, self.index_y + y, self.border, self.spacing, self.line_color)
                if neigh != self:
                    yield neigh

class Maze(object):
    MAX_PATH_LENGTH = 10

    def __init__(self, grid_size):
        self.visited_cells = []
        self.unvisited_cells = []
        self.cells_stack = []
        self._current_cell = None
        self.grid_size = grid_size
        self.current_path_length = 0

    @property
    def current_cell(self):
        return self._current_cell

    @current_cell.setter
    def current_cell(self, cell):
        self._current_cell = cell
        self.unvisited_cells.remove(cell)

    def init_cells(self, border, spacing):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.unvisited_cells.append(Cell(x, y, border, spacing))

        self.current_cell = choice(self.unvisited_cells)

    def break_wall(self):
        if not self.unvisited_cells:
            raise Exception('ACABOU')

        neighbors = [n for n in self.current_cell.neighbors(self.grid_size) if n in self.unvisited_cells]
        if (not neighbors and self.unvisited_cells) or self.current_path_length > self.MAX_PATH_LENGTH:
            self.current_cell = choice(self.unvisited_cells)
            self.current_path_length = 0
            return

        neighbor = choice(neighbors)
        self.visited_cells.append(self.current_cell)
        self.current_cell.link(neighbor)
        self.current_cell = neighbor
        self.current_path_length += 1

def setup():
    global maze

    randomSeed(1)
    size(700, 700)
    colorMode(HSB)
    strokeCap(ROUND)
    strokeWeight(5)
    border = 5
    spacing = (width - border * 2) / GRID_SIZE
    maze = Maze(GRID_SIZE)
    maze.init_cells(border, spacing)
    background("#c1bdb4")


def draw():
    try:
        maze.break_wall()
    except Exception:
        saveFrame()
        noLoop()
    println(len(maze.unvisited_cells))
