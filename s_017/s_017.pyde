def setup():
    size(800, 800)
    colorMode(HSB, 360, 100, 100)
    background(color(180, 80, 10))

def draw():
    main_color = color(180, 80, 10)
    noStroke()
    fill(main_color, 35)
    rect(0, 0, width, height)
    diff_x, diff_y = noise(14 + frameCount * 0.02), noise(15 + frameCount * 0.03)
    colors = range(1, 361, 360 / 24)

    strokeWeight(2)
    stroke(color(0, 30, 60))
    for c in colors:# select color
        cor = color(c, 100)
        fill(cor)
        pushMatrix()
        translate(height / 2, width / 2)
        rotate(radians(frameCount / 3))
        rotate(radians(c))
        arc(
            map(diff_x, 0, 1, 0, 20), 
            map(diff_y, 0, 1, 80, 110), 
            600, 500, 
            0, 
            PI / 24, 
            PIE
        )
        popMatrix()
        
    pushMatrix()    
    translate(height / 2, width / 2)
    fill(color(0, 80, 60))
    ellipse(0, 0, map(diff_x, 0, 1, 90, 110), map(diff_y, 0, 1, 90, 110))
    popMatrix()
