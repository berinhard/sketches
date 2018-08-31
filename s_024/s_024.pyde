"""
Súbita Logo
by Bernardo Fontes
forked from Daniel Shiffman's Recursive Tree.    

Renders a simple tree-like structure via recursion. 
The branching angle is calculated as a function of 
the given frameCount with a noise
"""

colors = [
    #(126,7,126),
    (176, 10, 176),
    (176, 10, 176),
    #(124,4,180),
    #(120,150,169),
    (142,186,230),
    (142,186,230),
    #(62,253,153),
    (2, 277, 111),
]

colors = [
    (255, 255, 255),
    (255, 255, 255, 90),
    (255, 255, 255, 80),
    (255, 255, 255, 70),
    (255, 255, 255, 60),    
]

diff_rotation = [noise(x * 864) for x in range(1, 100)]
diff_branch = [noise(x / 10000) for x in range(1, 100)]

def setup():
    size(700, 700)
    frameRate(100)

def draw():
    draw_tree()
    
    
def draw_tree():
    background(0)
    frameRate(30)
    strokeWeight(10)    
     
    # Let's pick an angle 0 to 90 degrees based on the mouse position
    a = (frameCount % width / float(width)) * 77
    # Convert it to radians
    # Start the tree from the bottom of the screen
    translate(width / 2, height)

    stroke(*colors[0])
    line(0, 0, 0, -160)
    # Move to the end of that line
    translate(0, -160)
    # Start the recursive branching!    
    branch(125, radians(a), 0)
    
    frame_name = "tree-019.png"
    if frameCount >= width - 1:
        saveFrame(frame_name)
        noLoop() 

def branch(h, theta, color_index):
    h *= 0.66  # branch size
    stroke_weight = map(h, 0, 125, 2, 10)
    strokeWeight(stroke_weight)
    branch_color = colors[color_index % len(colors)]
    if h > 1.3:  # min size is 1.3
        pushMatrix() 
        rotate(theta * diff_rotation[color_index])  #  add life to right branch angles
        stroke(*branch_color)
        new_h = h + (h / 2 * diff_branch[color_index])
        line(0, 0, 0, -h)  # Draw the branch
        translate(0, -h)  # Move to the end of the branch
        
        branch(h, theta, color_index + 1)  
        # Whenever we get back here, we "pop" in order to restore the previous
        # matrix state
        popMatrix()
        # Repeat the same thing, only branch off to the "left" this time!
        with pushMatrix():
            rotate(-theta)
            stroke(*branch_color)
            strokeWeight(stroke_weight)
            line(0, 0, 0, -new_h)
            translate(0, -new_h)
            branch(h, theta, color_index + 1)
