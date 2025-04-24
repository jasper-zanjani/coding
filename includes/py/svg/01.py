import drawsvg as draw
import math

d = draw.Drawing(width=200, height=200, origin='center', background='#FFDAB9')  # Light peach background

# --- Helper function to calculate hexagon vertices ---
def hexagon_vertices(center_x, center_y, radius):
    points = []
    for i in range(6):
        angle = 2 * 3.14159 * i / 6
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points

# --- Helper function to draw a triangle ---
def draw_triangle(draw_obj, p1, p2, p3, fill=None, stroke='peru', stroke_width=0.5):
    path = draw.Path(fill=fill, stroke=stroke, stroke_width=stroke_width)
    path.M(p1[0], p1[1])
    path.L(p2[0], p2[1])
    path.L(p3[0], p3[1])
    path.Z()
    draw_obj.append(path)

# --- Parameters for the grid ---
hexagon_radius = 80
triangle_side = hexagon_radius / math.sqrt(3)
center_x = 0
center_y = 0

# --- Draw the outer hexagon ---
hexagon_points = hexagon_vertices(center_x, center_y, hexagon_radius)
outer_hexagon = draw.Polygon(*[coord for p in hexagon_points for coord in p],
                             fill='none', stroke='peru', stroke_width=1)
d.append(outer_hexagon)

# --- Draw the internal triangles ---
import math

# Calculate the coordinates of the central point
central_point = (center_x, center_y)

# Draw the 6 triangles radiating from the center
for i in range(6):
    angle1 = 2 * math.pi * i / 6
    angle2 = 2 * math.pi * (i + 1) / 6
    p1 = central_point
    p2_x = center_x + hexagon_radius * math.cos(angle1)
    p2_y = center_y + hexagon_radius * math.sin(angle1)
    p2 = (p2_x, p2_y)
    p3_x = center_x + hexagon_radius * math.cos(angle2)
    p3_y = center_y + hexagon_radius * math.sin(angle2)
    p3 = (p3_x, p3_y)
    draw_triangle(d, p1, p2, p3, stroke_width=0.5)

# --- Draw the smaller internal lines to create the grid ---
# We can iterate through the edges of the outer hexagon and draw lines inwards

for i in range(6):
    p1_outer = hexagon_points[i]
    p2_outer = hexagon_points[(i + 1) % 6]

    # Find the midpoint of the outer edge
    mid_x = (p1_outer[0] + p2_outer[0]) / 2
    mid_y = (p1_outer[1] + p2_outer[1]) / 2

    # Draw a line from the midpoint to the center
    line = draw.Line(mid_x, mid_y, center_x, center_y, stroke='peru', stroke_width=0.5)
    d.append(line)

    # Draw the two lines connecting the midpoint to the adjacent vertices
    line1 = draw.Line(mid_x, mid_y, p1_outer[0], p1_outer[1], stroke='peru', stroke_width=0.5)
    d.append(line1)
    line2 = draw.Line(mid_x, mid_y, p2_outer[0], p2_outer[1], stroke='peru', stroke_width=0.5)
    d.append(line2)

# --- Coloring the specific triangles ---
def get_triangle_center(p1, p2, p3):
    return ((p1[0] + p2[0] + p3[0]) / 3, (p1[1] + p2[1] + p3[1]) / 3)

shaded_color = '#E9967A' # Light salmon

# --- Color the top row ---
top_triangles = [
    (hexagon_points[5], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 5 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 5 / 6)
    ), (
        (hexagon_points[5][0] + hexagon_points[0][0]) / 2,
        (hexagon_points[5][1] + hexagon_points[0][1]) / 2
    )),
    (hexagon_points[0], (
        center_x + hexagon_radius * math.cos(0),
        center_y + hexagon_radius * math.sin(0)
    ), (
        (hexagon_points[5][0] + hexagon_points[0][0]) / 2,
        (hexagon_points[5][1] + hexagon_points[0][1]) / 2
    )),
    (hexagon_points[0], (
        center_x + hexagon_radius * math.cos(0),
        center_y + hexagon_radius * math.sin(0)
    ), (
        (hexagon_points[0][0] + hexagon_points[1][0]) / 2,
        (hexagon_points[0][1] + hexagon_points[1][1]) / 2
    )),
    (hexagon_points[1], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 1 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 1 / 6)
    ), (
        (hexagon_points[0][0] + hexagon_points[1][0]) / 2,
        (hexagon_points[0][1] + hexagon_points[1][1]) / 2
    )),
]
for triangle in top_triangles:
    draw_triangle(d, triangle[0], triangle[1], triangle[2], fill=shaded_color, stroke_width=0.5)

# --- Color the bottom row ---
bottom_triangles = [
    (hexagon_points[3], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 3 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 3 / 6)
    ), (
        (hexagon_points[3][0] + hexagon_points[2][0]) / 2,
        (hexagon_points[3][1] + hexagon_points[2][1]) / 2
    )),
    (hexagon_points[2], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 2 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 2 / 6)
    ), (
        (hexagon_points[3][0] + hexagon_points[2][0]) / 2,
        (hexagon_points[3][1] + hexagon_points[2][1]) / 2
    )),
    (hexagon_points[2], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 2 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 2 / 6)
    ), (
        (hexagon_points[2][0] + hexagon_points[1][0]) / 2,
        (hexagon_points[2][1] + hexagon_points[1][1]) / 2
    )),
    (hexagon_points[1], (
        center_x + hexagon_radius * math.cos(2 * math.pi * 1 / 6),
        center_y + hexagon_radius * math.sin(2 * math.pi * 1 / 6)
    ), (
        (hexagon_points[2][0] + hexagon_points[1][0]) / 2,
        (hexagon_points[2][1] + hexagon_points[1][1]) / 2
    )),
]
for triangle in bottom_triangles:
    draw_triangle(d, triangle[0], triangle[1], triangle[2], fill=shaded_color, stroke_width=0.5)

# --- Color the central diamond shape ---
central_diamond_triangles = [
    (central_point, (hexagon_points[5][0] + hexagon_points[0][0]) / 2, (hexagon_points[5][1] + hexagon_points[0][1]) / 2, hexagon_points[0]),
    (central_point, hexagon_points[0], (hexagon_points[0][0] + hexagon_points[1][0]) / 2, (hexagon_points[0][1] + hexagon_points[1][1]) / 2),
    (central_point, (hexagon_points[3][0] + hexagon_points[2][0]) / 2, (hexagon_points[3][1] + hexagon_points[2][1]) / 2, hexagon_points[3]),
    (central_point, hexagon_points[3], (hexagon_points[2][0] + hexagon_points[1][0]) / 2, (hexagon_points[2][1] + hexagon_points[1][1]) / 2),
]

# Need to carefully define the vertices of the central shaded region
central_shaded_points = [
    (hexagon_points[5][0] + hexagon_points[0][0]) / 2, (hexagon_points[5][1] + hexagon_points[0][1]) / 2,
    (hexagon_points[0][0] + hexagon_points[1][0]) / 2, (hexagon_points[0][1] + hexagon_points[1][1]) / 2,
    (hexagon_points[1][0] + hexagon_points[2][0]) / 2, (hexagon_points[1][1] + hexagon_points[2][1]) / 2,
    (hexagon_points[2][0] + hexagon_points[3][0]) / 2, (hexagon_points[2][1] + hexagon_points[3][1]) / 2,
    (hexagon_points[3][0] + hexagon_points[4][0]) / 2, (hexagon_points[3][1] + hexagon_points[4][1]) / 2,
    (hexagon_points[4][0] + hexagon_points[5][0]) / 2, (hexagon_points[4][1] + hexagon_points[5][1]) / 2,
]
central_shaded_polygon = draw.Polygon(*central_shaded_points, fill=shaded_color, stroke='peru', stroke_width=0.5)
d.append(central_shaded_polygon)


d.save_svg('hexagon_grid.svg')

from IPython.display import SVG
SVG('hexagon_grid.svg')
