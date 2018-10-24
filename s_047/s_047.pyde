img = None

def settings():
    global img
    
    img = loadImage("/home/bernardo/Pictures/Webcam/selfie.jpg")
    size(img.width, img.height)

def setup():
    background(255)
    strokeWeight(2)
    
def draw():
    n = noise(frameCount / 100.0)
    
    x1, y1 = int(random(width)), int(random(height))
    x2, y2 = int(random(width)), int(random(height))
    amounts = [p / 100.0 for p in range(100)]
    for amt in amounts:
        x = int(lerp(x1, x2, amt))
        y = int(lerp(y1, y2, amt))
        
        index = x + y * img.width
        pixel = img.pixels[index]
        r, g, b = red(pixel), blue(pixel), green(pixel)
        c = color(r, 0, 0, 80)
        stroke(c)
        point(x, y)
        
        
def keyPressed():
    if key == 's':
        saveFrame("portrait.png")
