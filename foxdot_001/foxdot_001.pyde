# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.palettes import get_color_palette
from random import choice

add_library('oscP5')

oscP5 = None

def setup():
    #fullScreen()
    size(900, 900)
    background(255)
    global oscP5
    oscP5 = OscP5(this, 12000)
    oscP5.addListener(MyOscListener())
    print oscP5.listeners()
    loc = NetAddress('127.0.0.1', 12000)
    strokeWeight(4)

freq = 0
freqs = set()

def draw():
    background(27)
    #display_bass()
    display_bass_2()
    display_pads()    
    display_keys()
    

def display_bass_2():
    beginShape()
    strokeWeight(8)
    stroke(250)
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


def display_keys():
    global key_strokes
    
    for i, value in enumerate(key_strokes):
        y, l_size = value
        x = random(width)
        stroke(250)
        strokeWeight(14)
        line(x, y, x + l_size, y)        
        key_strokes[i][1] -= 1
        
    key_strokes = [[y, v] for y, v in key_strokes if v > 0]
            
            
def display_bass():
    if freq:
        w = map(freq, 200, 500, 0, width)
        h = map(freq, 200, 500, 0, height)
        rect(0, 20, w, 200)
        rect(width - w, height - 220, w, 200)
        
        rect(width - 220, 0, 200, h)
        rect(0, height - h, 200, height)
        
def display_pads():
    if particles:
        for particle in particles:
            particle.atualiza()
            particle.desenha()        

def stop():
    global oscP5
    oscP5.dispose()
    

colors = get_color_palette()

class Particle(object):
    
    def __init__(self):
        self.x = random(width)
        self.y = height
        self.altura_maxima = int(random(300))
        self.color = choice(colors)
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

key_strokes = []
particles = []
class MyOscListener(OscEventListener):
    
    @staticmethod
    def oscEvent(m):   
        global freq 
        args = m.arguments()
        valid_instruments = ['bass', 'pads', 'sawbass', 'keys']
        
        if str(args[0]) not in valid_instruments:
            return
        
        name = str(args[0])
        if name in ['bass', 'sawbass']:
            freq = int(args[7])
            freqs.add(freq)
        elif name == 'pads':
            particles.append(Particle())
        elif name == 'keys':
            if len(key_strokes) < 1000:
                key_strokes.append(
                    [int(random(height)), int(random(100, 600))]
                )
                
            
