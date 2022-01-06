class Piece:
    def __init__(self, piece, color, pos):
        self.pos = pos
        self.color = color
        self.piece = piece
        self.pieces_dict = {
            'king': {'black': ' ♔ ', 'white': ' ♚ '},
            'queen': {'black': ' ♕ ', 'white': ' ♕ '},
            'rook': {'black': ' ♖ ', 'white': ' ♜ '},
            'bishop': {'black': ' ♗ ', 'white': ' ♝ '},
            'knight': {'black': ' ♘ ', 'white': ' ♞ '},
            'pawn': {'black': ' ♙ ', 'white': ' ♟ '}
        }
        self.symbol_piece = self.pieces_dict[self.piece][self.color]
        self.pos = pos


class King(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        super().__init__(color=self.color, piece='king', pos=self.pos)


class Queen(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 9
        super().__init__(piece='queen', color=self.color, pos=self.pos)


class Rook(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 5
        super().__init__(piece='rook', color=self.color, pos=self.pos)


class Bishop(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 3
        super().__init__(piece='bishop', color=self.color, pos=self.pos)


class Knight(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 4
        super().__init__(piece='knight', color=self.color, pos=self.pos)


class Pawn(Piece):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 1
        super().__init__(piece='pawn', color=self.color, pos=self.pos)
