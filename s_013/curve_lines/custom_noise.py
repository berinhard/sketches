# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

class NoiseWave:
    """
    Class to enable noise increment propagation through an array
    """

    def __init__(self, array_size, init_value=0):
        self.init_value = init_value
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

    def index_noise(self, i, not_started_value=0):
        if self.noises[i] == self.init_value:
            return not_started_value
        return noise(self.noises[i])
