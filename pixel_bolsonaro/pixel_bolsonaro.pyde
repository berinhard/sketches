img = None
RECT_SIZE = 20

def setup():
    global img
    
    size(768, 512)
    img = loadImage("/home/bernardo/Desktop/bozo.jpg")

def draw():   
    num_cols = width / RECT_SIZE
    num_lines = height / RECT_SIZE
    
    #image(img, 0, 0)
    img.loadPixels()
    for x in range(0, width, RECT_SIZE):
        for y in range(0, height, RECT_SIZE):
            index = x + y * width
            pixel_color = img.pixels[index]
            
            r = red(pixel_color)
            g = green(pixel_color)
            b = blue(pixel_color)
            c = color(r, g, b)

            fill(c)
            noStroke()
            rect(x, y, RECT_SIZE, RECT_SIZE)
        
    img.updatePixels()
    noLoop()
