from board import Board


class Engine():
    def __init__(self):
        self.piece_pos = Board().board_notacion
        self.move_table = Board().tablero_de_jugadas
    
    def player_move(self, move):
        pass

    def machine_move(self, move):
        pass

    def move_piece(self, piece):
        pass

    def get_index_move(self, move) -> tuple:
        """ CASE:
        True = (True, indice)
        False = (False,)
        """

        for row in self.piece_pos:
            if move in row:
                index_piece = True
                return index_piece, row.index(move), self.piece_pos.index(row)
            else: index_piece = (False,)

        return index_piece

    def set_pos_piece(self, piece, move):
        if self.get_index_move(move)[0]:
            exist, new_pos, row = self.get_index_move(move)
            self.move_table[row][new_pos] = piece.symbol_piece





        



