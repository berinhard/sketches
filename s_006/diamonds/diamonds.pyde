class NoiseWave:
    """
    Class to enable noise increment propagation through an array
    """

    def __init__(self, array_size, init_value=0):
        self.array_size = array_size
        self.noises = [init_value] * array_size

    @property
    def max_index(self):
        return self.array_size - 1

    def increment(self, step):
        for i in range(self.max_index, -1, -1):
            if i == 0:
                self.noises[i] += step  # only increments first value
            else:
                # other values should copy the step from the previous position
                self.noises[i] = self.noises[i-1]

    def index_noise(self, i):
        return noise(self.noises[i])  # get noise by position


class Diamond:

    def __init__(self, horizontal_position, offset_y, reversed=False):
        self.horizontal_position = horizontal_position
        self.offset_y = offset_y
        self.reversed = reversed
        self.max_lines = 40
        self.top_lines, self.bottom_lines = [], []
        self.alpha = 40


    def draw(self, noise_x, noise_y):
        y1, y2 = self.y_values

        if self.reversed:
            x = self.offset_x + 100 - (100 * noise_x)
            y = self.offset_y + (200 * noise_y)
        else:
            x = self.offset_x + (100 * noise_x)
            y = self.offset_y + 200 - 200 * noise_y

        self.add_line(self.x, y1, x, y)
        self.add_line(self.x, y2, x, y, is_top=False)
        self.draw_lines()

    @property
    def x(self):
        """
        Translate the diamond respecting its position
        """
        return (self.horizontal_position + 1) * 100

    @property
    def offset_x(self):
        return self.x - 50

    @property
    def y_values(self):
        """
        Returns top and bottom of the diamond
        """
        return self.offset_y, self.offset_y + 200

    def draw_lines(self):
        colours = [50, 120, 140]
        if self.reversed:
            colours = reverse(colours)

        stroke(colours[0], colours[1], colours[2], self.alpha)
        for x1, y1, x2, y2 in self.top_lines:
            line(x1, y1, x2, y2)

        colours = reverse(colours)
        stroke(colours[0], colours[1], colours[2], self.alpha)
        for x1, y1, x2, y2 in self.bottom_lines:
            line(x1, y1, x2, y2)

    def add_line(self, x1, y1, x2, y2, is_top=True):
        """
        Keeps a maximum of max_lines of internal golden lines
        """
        if is_top:
            lines = self.top_lines
        else:
            lines = self.bottom_lines

        if len(lines) > self.max_lines:
            lines.pop(0)
        lines.append((x1, y1, x2, y2))

    @property
    def oldest_point(self):
        return self.top_lines[0][2:]


    @property
    def newest_point(self):
        return self.top_lines[-1][2:]

top_lines = [
    Diamond(col, 20) for col in range(7)
]
bottom_lines = [
    Diamond(col, 240, reversed=True) for col in range(7)
]
noise_x = NoiseWave(len(top_lines))
noise_y = NoiseWave(len(top_lines), init_value=8)

def setup():
    size(800, 460)
    frameRate(16)
    background(0)
    strokeWeight(2)

def draw():
    background(0)
    for i, diamonds in enumerate(zip(top_lines, bottom_lines)):
        diamonds[0].draw(noise_x.index_noise(i), noise_y.index_noise(i))
        diamonds[1].draw(noise_x.index_noise(i), noise_y.index_noise(i))

    noise_x.increment(0.1)
    noise_y.increment(0.02)
