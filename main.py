from board import Board
from pieces import *
from engine import Engine

# all pieces
# white pieces
w_king = King('white', 'e1')
w_queen = Queen('white', 'd1')
w_rook_left = Rook('white', 'h1')
w_rook_right = Rook('white', 'a1')
w_bishop_w = Bishop('white', 'c1')
w_bishop_b = Bishop('white', 'f1')
w_knight_left = Knight('white', 'b1')
w_knight_right = Knight('white', 'g1')

w_pawn_1 = Pawn('white', 'a2')
w_pawn_2 = Pawn('white', 'b2')
w_pawn_3 = Pawn('white', 'c2')
w_pawn_4 = Pawn('white', 'd2')
w_pawn_5 = Pawn('white', 'e2')
w_pawn_6 = Pawn('white', 'f2')
w_pawn_7 = Pawn('white', 'g2')
w_pawn_8 = Pawn('white', 'h2')


# black pieces
b_king = King('black', 'e8')
b_queen = Queen('black', 'd8')
b_rook_left = Rook('black', 'h8')
b_rook_right = Rook('black', 'a8')
b_bishop_w = Bishop('black', 'c8')
b_bishop_b = Bishop('black', 'f8')
b_knight_left = Knight('black', 'b8')
b_knight_right = Knight('black', 'g8')

b_pawn_1 = Pawn('black', 'a7')
b_pawn_2 = Pawn('black', 'b7')
b_pawn_3 = Pawn('black', 'c7')
b_pawn_4 = Pawn('black', 'd7')
b_pawn_5 = Pawn('black', 'e7')
b_pawn_6 = Pawn('black', 'f7')
b_pawn_7 = Pawn('black', 'g7')
b_pawn_8 = Pawn('black', 'h7')

white_pieces = [
    w_king, w_queen, 
    w_rook_left, 
    w_rook_right, 
    w_bishop_b, 
    w_bishop_w, 
    w_knight_left, 
    w_knight_right,
    w_pawn_1,
    w_pawn_2,
    w_pawn_3,
    w_pawn_4,
    w_pawn_5,
    w_pawn_6,
    w_pawn_7,
    w_pawn_8
]

black_pieces = [
    b_king, 
    b_queen, 
    b_rook_left, 
    b_rook_right, 
    b_bishop_b, 
    b_bishop_w, 
    b_knight_left, 
    b_knight_right,
    b_pawn_1,
    b_pawn_2,
    b_pawn_3,
    b_pawn_4,
    b_pawn_5,
    b_pawn_6,
    b_pawn_7,
    b_pawn_8
]


board = Board()
chessEngine = Engine()
chessEngine.set_pos_piece(white_pieces[0],'e57')
board.print_asci_board()