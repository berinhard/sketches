class Particle(object):
    
    def __init__(self, c):
        self.x = random(width)
        self.y = height
        self.altura_maxima = int(random(300))
        self.color = c
        self.r = 50
        
    def atualiza(self):
        self.x += random(-3, 3)
        self.y -= 1
        self.r = map(self.y, height, self.altura_maxima, 50, 0)
        
    def desenha(self):
        if self.y < self.altura_maxima:
            return
        
        stroke(27, 27, 27, 90)
        fill(self.color)
        ellipse(self.x, self.y, self.r, self.r)
        
    def sumiu(self):
        return self.r <= 1
