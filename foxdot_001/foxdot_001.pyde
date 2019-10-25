# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.palettes import get_color_palette
from collections import deque
from particles import Particle
from synth_displays import *

add_library('oscP5')
oscP5 = None

def setup():
    global oscP5
    oscP5 = OscP5(this, 12000)
    oscP5.addListener(MyOscListener())
    loc = NetAddress('127.0.0.1', 12000)
    
    #fullScreen()
    size(1024, 768)
    background(255)
    
        
class DrawHandler(object):

    def __init__(self):
        self.active_displays = []
        self.displays = []
        
    def add(self, display):
        self.displays.append(display)
        
    def shuffle(self):
        self.active_displays = [d for d in self.displays if random(1) > 0.5]
        if not self.active_displays:
            self.shuffle()
            
    def update(self):
        counter = 0
        loop_limit = 10
        while synths_deque and counter <= loop_limit:
            counter += 1
            synth_data = synths_deque.pop()
            for display in self.active_displays:
                display.update(synth_data)
                
    def draw(self):
        for display in self.active_displays:
            display.draw()

draw_handler = DrawHandler()
draw_handler.add(BassDisplay1())
draw_handler.add(BassDisplay2())
draw_handler.add(PadsDisplay1())
draw_handler.add(KeysDisplay1())

def draw():
    if frameCount == 1 or not frameCount % 1000:
        draw_handler.shuffle() 
    
    background(27)    
    draw_handler.update()
    draw_handler.draw()
    
    if not frameCount % 10: 
        synths_deque.clear()

synths_deque = deque()
class MyOscListener(OscEventListener):
    
    @staticmethod
    def oscEvent(m):    
        args = m.arguments()
        name = args[0]
        is_synth_message = all([
            m.addrPattern() == u'/s_new',
            name != u'startSound',
            name != u'makeSound',
            not str(name).startswith(u'play'),
        ])
        if not is_synth_message:
            return    
    
        synth_data = {
            u"name": args[0],
            u"id": args[1],
            u"add_action": args[2],
            u"target_id": args[3],            
        }
        
        offset = 4
        for i, value in enumerate(args[offset:]):
            if isinstance(value, unicode):
                synth_data[value] = args[offset + i + 1]
                
        print(u"Processing: " + synth_data['name'] + u' - Frequency: ' + str(synth_data.get('freq', 0)))
        synths_deque.appendleft(synth_data)                

def stop():
    global oscP5
    oscP5.dispose()
