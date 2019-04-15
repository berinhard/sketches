WIDTH, HEIGHT = 900, 900
px, py = 42, - HEIGHT / 2.1
start_angle = TWO_PI
angle = start_angle
CLOCK_FRAME_PACE = 500


def setup():
    size(WIDTH, HEIGHT)
    background(255)        
    frameRate(1000)
    stroke(50, 50)
    strokeWeight(0.5)
    blendMode(MULTIPLY)

def draw():
    global px, py, angle
    
    pushMatrix()
    translate(width / 2, height / 2)
    
    if (not frameCount % CLOCK_FRAME_PACE):
        turn = frameCount / CLOCK_FRAME_PACE
        
        if turn < 10:
            stroke(50 + turn * 15, 50)
            angle = start_angle + turn * QUARTER_PI / 2
        elif turn == 10:
            blendMode(BLEND)
            stroke(124, 10, 2, 30)
            angle = start_angle + turn * QUARTER_PI / 2
        elif turn > 12:
            saveFrame("####.png")
            noLoop()
        
    rotate(angle)
    margin_x = width / 7
    
    x = map(noise(frameCount * 0.006), 0, 1, px - margin_x, px + margin_x)    
    y = map(noise(10 + frameCount * 0.008), 0, 1, py + 100, py + 350)
     
    line(px, py, x, y)
    popMatrix()
    
