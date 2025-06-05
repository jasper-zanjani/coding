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

    # Draw knight anchored on position (self.x, self.y)
    anchor = Graphene.Point().init(self.x, self.y)
    factor = self.PIECE_SIZE / self.knight_bounds.get_width()
    transformation = Gsk.Transform().translate(anchor).scale(factor, factor)
    snapshot.transform(transformation)
    snapshot.append_stroke(self.knight_path, self.knight_stroke, self.knight_color)

