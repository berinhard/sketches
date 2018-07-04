from random import choice

GRID_SIZE = 40

class Cell(object):

    def __init__(self, x, y, border, spacing):
        self.index_x, self.index_y = x, y
        self.border = border
        self.spacing = spacing

    @property
    def x(self):
        return self.border + self.spacing / 2 + self.index_x * self.spacing

    @property
    def y(self):
        return self.border + self.spacing / 2 + self.index_y * self.spacing

    def plot(self):
        point(self.x, self.y)

    def link(self, cell):
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
                neigh = Cell(self.index_x + x, self.index_y + y, self.border, self.spacing)
                if neigh != self:
                    yield neigh

class Maze(object):

    def __init__(self, grid_size):
        self.visited_cells = []
        self.unvisited_cells = []
        self.cells_stack = []
        self._current_cell = None
        self.grid_size = grid_size

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
        if not neighbors and self.unvisited_cells:
            self.current_cell = choice(self.unvisited_cells)
            return

        neighbor = choice(neighbors)
        self.visited_cells.append(self.current_cell)
        self.current_cell.link(neighbor)
        self.current_cell = neighbor

def setup():
    global maze

    randomSeed(1)
    size(700, 700)
    colorMode(HSB)
    strokeCap(PROJECT)
    strokeWeight(5)
    border = 5
    spacing = (width - border * 2) / GRID_SIZE
    maze = Maze(GRID_SIZE)
    maze.init_cells(border, spacing)
    background(255)


def draw():
    try:
        maze.break_wall()
    except Exception:
        saveFrame()
        noLoop()
    println(len(maze.unvisited_cells))
