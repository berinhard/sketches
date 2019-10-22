# berin lib: https://github.com/berinhard/berin/
from berin.palettes import get_color_palette
from itertools import cycle
from random import choice
from particles import Particle


colors = get_color_palette()


class BassDisplay1(object):
    
    def __init__(self):
        self.freq = 0
        self.colors = cycle(colors)
        self.c = next(self.colors)
        
    def update(self, synth_data):
        if not synth_data['name'] in ['bass', 'sawbass']:
            return
        
        self.freq = synth_data['freq']
        self.c = next(self.colors)
        
    def draw(self):
        fill(self.c)
        strokeWeight(4)
        stroke(240)
        freq = self.freq
        if freq:
            w = map(freq, 200, 500, 0, width)
            h = map(freq, 200, 500, 0, height)
            rect(0, 20, w, 200)
            rect(width - w, height - 220, w, 200)
            
            rect(width - 220, 0, 200, h)
            rect(0, height - h, 200, height)
            
            
class BassDisplay2(object):
    
    def __init__(self):
        self.freqs = set()
        
    def update(self, synth_data):
        if not synth_data['name'] in ['bass', 'sawbass']:
            return
        
        self.freqs.add(synth_data['freq'])
        
    def draw(self):
        beginShape()
        strokeWeight(8)
        stroke(250)
        freqs = self.freqs
        
        fill(choice(colors))
        for x in freqs:
            y = random(height)
            vertex(x, y)
        endShape(TRIANGLE_STRIP)
        
        fill(choice(colors))
        beginShape()
        for x in freqs:
            y = random(height)
            vertex(y, x)
        endShape(TRIANGLE_STRIP)
        
        
        fill(choice(colors))
        for x in freqs:
            y = random(height)
            vertex(width - x, height - y)
        endShape(TRIANGLE_STRIP)
        
        fill(choice(colors))
        beginShape()
        for x in freqs:
            y = random(height)
            vertex(width - y, height - x)
        endShape(TRIANGLE_STRIP)
        
        
class PadsDisplay1(object):
    
    def __init__(self):
        self.particles = []
        
    def update(self, synth_data):
        if synth_data['name'] == 'pads':
            self.particles.append(Particle(choice(colors)))
            
    def draw(self):
        to_remove = []
        for particle in self.particles:
            particle.atualiza()
            particle.desenha()
            if particle.sumiu():
                to_remove.append(particle)
                
        for p in to_remove:
            self.particles.remove(p)


class KeysDisplay1(object):
    
    def __init__(self):
        self.key_strokes = []

    def update(self, synth_data):
        if synth_data['name'] == 'keys':
            if len(self.key_strokes) < 1000:
                self.key_strokes.append(
                    [int(random(height)), int(random(100, 600))]
                )

    def draw(self):
        for i, value in enumerate(self.key_strokes):
            y, l_size = value
            x = random(width)
            stroke(250)
            strokeWeight(14)
            line(x, y, x + l_size, y)        
            self.key_strokes[i][1] -= 1
            
        self.key_strokes = [[y, v] for y, v in self.key_strokes if v > 0]
