img = None
RECT_SIZE = 5

def setup():
    global img

    size(800, 600)
    img = loadImage("test.jpg")
    #img = loadImage("/home/bernardo/Pictures/Webcam/2018-07-10-154544.jpg")
    #img = loadImage("/home/bernardo/Pictures/Webcam/2018-10-18-100241.jpg")

    #frameRate(10)

def save_video_frames(frame_rate, seconds, stop_run=True, extension="png", log_frame=True):
    num_frames = frame_rate * seconds

    if log_frame:
        print("{} /  {} - {}%".format(
            frameCount, int(num_frames), int(frameCount * 100 / num_frames)
        ))
    if frameCount <= num_frames:
        frame_name ="#" * (len(str(num_frames)))
        saveFrame("{}.{}".format(frame_name, extension))
    elif stop_run:
        noLoop()

def draw():
    #RECT_SIZE = int(map(random(1), 0,1, 5, 20))
    RECT_SIZE = 10

    num_cols = width / RECT_SIZE
    num_lines = height / RECT_SIZE

    img.loadPixels()
    for x in range(0, width, RECT_SIZE):
        for y in range(0, height, RECT_SIZE):
            v = noise(x / 367.3, y / 95.341, frameCount / 100.0)
            base_x = int(map(v, 0, 1, 0, width))

            index = base_x + x + y * width
            pixel_color = img.pixels[index]

            r = red(pixel_color)
            g = green(pixel_color)
            b = blue(pixel_color)
            c = color(r, g, b)

            if v > 0.7:
                c = color(g, b, (r ** 2) % 255)
            elif v > 0.6:
                c = color(g, (r ** 2) % 255, b)
            elif v > 0.55:
                c = color((r ** 2) % 255, b, g)

            fill(c)
            noStroke()
            rect(x, y, RECT_SIZE, RECT_SIZE)

    img.updatePixels()
    #save_video_frames(60, 60)

def keyPressed():
    if key == 's':
        saveFrame("#######.png")