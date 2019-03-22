# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

TOTAL_FRAMES = 84
WIDTH, HEIGHT = 500, 500
WHITE = color(239, 239, 239)
BLACK = color(27, 27, 27)
BLUE = color(55,189,202)
COMPLEMENTARY = BLUE

def get_gif_percent(total_frames, counter=None):
    counter = counter or frameCount
    return float(counter) % total_frames / total_frames


def get_all_points(num_points, n_sides):
    if not getattr(get_all_points, '_cached_return', None):
        get_all_points._cached_return = {}


    key = '{},{}'.format(num_points, n_sides)
    if not key in get_all_points._cached_return:
        all_points = []
        x, y = width / 2, height / 2
        points = regular_polygon(x, y, radius=225, n_sides=n_sides, draw=False)

        for i in range(num_points):
            all_points.append(points)

            new_points = []
            for i, point in enumerate(points):
                previous_point = points[i - 1]
                new_points.append(
                    PVector.lerp(previous_point, point, 0.95)
                )

            points = new_points

        get_all_points._cached_return[key] = all_points

    return get_all_points._cached_return[key]


def setup():
    size(WIDTH, HEIGHT)
    noFill()
    background(WHITE)
    all_points = get_all_points(TOTAL_FRAMES, 6)


def draw():
    background(WHITE)

    if frameCount > TOTAL_FRAMES * 2:
        noLoop()

    all_points = get_all_points(TOTAL_FRAMES, 6)
    total_points = len(all_points)
    percent = get_gif_percent(TOTAL_FRAMES)
    num_rects = int(easings.easeInOutSine(percent) * TOTAL_FRAMES)

    if not frameCount / TOTAL_FRAMES % 2:
        all_points = all_points[:num_rects + 1]
    else:
        all_points = all_points[:len(all_points) - num_rects]


    for i, points in enumerate(all_points):
        alpha = map(i, 0, total_points - 1, 230, 20)
        weight = map(i, 0, total_points - 1, 3, 1)
        strokeWeight(weight)
        stroke(color(27, 27, 27, alpha))
        draw_shape(points, end_shape_mode=CLOSE)

    saveFrame("#########.png")