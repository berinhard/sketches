from string import ascii_uppercase
from random import shuffle, choice
from points import ConnectablePoint

BLACK = color(17, 17, 17)
BLACK_CLEAN = color(17, 17, 17, 200)
RED_CLEAN = color(217, 17, 42, 200)
char_values = ascii_uppercase + '0123456789'
points = [] 


#####
# QR CODE sample: QBBRR8DWV8
# Q --> 17
# B --> 2
# B --> 2
# R --> 18
# R --> 18
# 8 --> 35
# D --> 4
# W --> 23
# V --> 22
# 8 --> 35
#####

def setup():
    size(600, 1000)
    background(255)
    strokeCap(ROUND)

    
class QRCodeRandomizer():
    
    def __init__(self, qrcode):
        self.qrcode = qrcode.upper()
        self._points = []
        
    @property
    def points(self):
        if not self._points:    
            max_sum = (len(char_values) - 1) * len(char_values)
            text_sum = sum(char_values.index(c) + 1 for c in self.qrcode)
            percent = float(text_sum) / max_sum
            rect_width, rect_height = width - 100, height - 100
            rect_area = rect_width * rect_height / 30.0
            
            num_points = percent * rect_area
            print(num_points)
            for i in range(ceil(num_points)):
                x = int(random(50, width - 50))
                y = int(random(50, height - 50))
                
                self._points.append(ConnectablePoint(x, y))
                
            to_link = self._points
            for i, p in enumerate(to_link):
                print("{} / {}".format(i, num_points))
                p.link_neighbors(to_link)
                
        return self._points
    
    def reb_prob(self, y):
        char_pos = int(map(y, 50, height - 50, 0, len(self.qrcode)))
        qrcode_char = self.qrcode[char_pos]
        return float(char_values.index(qrcode_char) + 1) / (len(char_values) + 1)  



dukao = "QA7W57EE70"
eu = "QCMRLGHWTZ"
luciano = "QA8E4KWHX7"
julio = "QGJHMRPAY5"
qrcode_randomizer = QRCodeRandomizer(eu) 


def draw():
    background(255)
    points = qrcode_randomizer.points
    for random_point in points:
        random_point.display_links(qrcode_randomizer)
        
    for random_point in points:
        random_point.display_points()
    
    fill(BLACK)
    signature = "{} - {} points".format(qrcode_randomizer.qrcode, len(points))
    text(signature, 50,  height - 25)
    saveFrame("{}.png".format(qrcode_randomizer.qrcode))
        
    noLoop()
