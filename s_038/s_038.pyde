# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

img = None

WHITE = color(200, 200, 200)
RED = color(184, 15, 10)
BLACK = color(10)


def setup():
    global img
    size(768, 512)
    #img = loadImage("/home/bernardo/Desktop/img.jpeg")
    #image(img, 0, 0)


def pixel_quantization(pixel, factor):
    r, g, b = red(pixel), green(pixel), blue(pixel)
    
    new_r = round(factor * r / 255.0) * 255 / factor
    new_g = round(factor * g / 255.0) * 255 / factor
    new_b = round(factor * b / 255.0) * 255 / factor    

    error_r = r - new_r
    error_g = g - new_g
    error_b = b - new_b
    
    return new_r, new_g, new_b, error_r, error_g, error_b


def draw():
    
    def index(x, y):
        return x + y * width
    
    img = loadImage("/home/bernardo/Desktop/test.JPG")
    img.filter(GRAY)
    img.loadPixels()

    # Floyd steinberg dithering
    for y in range(img.height - 1):
        
        active_line = False
        if noise((frameCount + y) / 10) > 0.4:
            active_line = True
             
        
        for x in range(1, img.width):        
            pixel = img.pixels[index(x, y)]
        
            new_r, new_g, new_b, error_r, error_g, error_b = pixel_quantization(pixel, 1)
        
            img.pixels[index(x, y)] = color(new_r, new_g, new_b)  # update current pixel
            
            if not active_line:
                continue
            
            indexes_and_diffusion_coef = [
                (index(x + 1, y    ), 7/ 16.0),
                (index(x - 1, y + 1), 3/ 16.0),
                (index(x    , y + 1), 5/ 16.0),
                (index(x + 1, y + 1), 1/ 16.0),  
            ]
            for n_index, diffusion_coef in indexes_and_diffusion_coef:  # push residual quantization error
                try:
                    n_color = img.pixels[n_index]
                    
                    r, g, b = red(n_color), blue(n_color), green(n_color)
                    r += error_r * diffusion_coef
                    g += error_g * diffusion_coef
                    b += error_b * diffusion_coef
                    
                    img.pixels[n_index] = color(r + 20, g, b)
                except IndexError:  # boundaries
                    continue

    #img.updatePixels()
    #image(img, 0, 0)
    #saveFrame("#####.png")
    #print(frameCount)
    #if frameCount > 6000:
    #    noLoop()
    
def keyPressed():
    if key == ' ':
        redraw()
