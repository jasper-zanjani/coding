import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gdk", "4.0")
from gi.repository import Adw, Gtk, Gdk, Graphene, Gsk

class Chessboard(Gtk.Widget):
    SQUARE_SIZE = 120
    BOARD_SIZE = 4 * SQUARE_SIZE
    PIECE_SIZE = 1.5 * SQUARE_SIZE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # initialize colors
        self.black_squares_color = Gdk.RGBA()
        self.black_squares_color.parse("DarkGreen")
        self.white_squares_color = Gdk.RGBA()
        self.white_squares_color.parse("DarkGrey")

    def do_snapshot(self, snapshot):
        # Draw chessboard by repeating a 2x2 block of squares
        bounds = Graphene.Rect().init(0, 0, self.BOARD_SIZE, self.BOARD_SIZE)
        child_bounds = Graphene.Rect().init(
            0, 0, 2 * self.SQUARE_SIZE, 2 * self.SQUARE_SIZE
        )
        snapshot.push_repeat(bounds, child_bounds)  # start of repeated part

        r11 = Graphene.Rect()
        r11.init(0, 0, self.SQUARE_SIZE, self.SQUARE_SIZE)
        snapshot.append_color(self.white_squares_color, r11)
        r12 = Graphene.Rect()
        r12.init(0, self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        snapshot.append_color(self.black_squares_color, r12)
        r21 = Graphene.Rect()
        r21.init(self.SQUARE_SIZE, 0, self.SQUARE_SIZE, self.SQUARE_SIZE)
        snapshot.append_color(self.black_squares_color, r21)
        r22 = Graphene.Rect()
        r22.init(self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        snapshot.append_color(self.white_squares_color, r22)

        snapshot.pop()  # end of repeated part

        # Attempting to display triangle
        p1 = Graphene.Point3D()
        p1.init(0.0, 0.0, 0.0)  # Vertex at origin

        p2 = Graphene.Point3D()
        p2.init(1.0, 0.0, 0.0)  # Vertex on the x-axis

        p3 = Graphene.Point3D()
        p3.init(0.0, 1.0, 0.0)  # Vertex on the y-axis
        triangle = Graphene.Triangle()
        blue = Gdk.RGBA()
        blue.parse("Blue")
        triangle.init_from_point3d(p1, p2, p3)
        snapshot.append_color(blue, triangle)

