
class Board():
    def __init__(self):
        # crear tablero de referencia
        self.board_notacion = [
            ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
            ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
            ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
            ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
            ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
            ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        ]
        # crear tablero para imprimir jugadas
        self.tablero_de_jugadas = self.create_game_board()

    def create_game_board(self):
        """
        ---- CREAR TABLERO ------\n
        \n
        crea una lista que sera impresa en la terminal
        basado en el tablero de coordenadas
        """
        board = []
        for i in range(8):
            board_letter = []
            for i in range(8):
                board_letter.append(' • ')
            board.append(board_letter)
        # recorre la lista y la convierte en puntos para
        # el tablero de texto
        return board

    def print_asci_board(self):
        """
        --- IMPRIMIR TABLERO ----\n
        \n
        imprime el tablero en la terminal
        """
        board_text = '\n\n'  # tablero de texto
        contador = 8
        for i in self.tablero_de_jugadas:
            board_text += '\n'
            board_text += '\t'
            for d in i:
                board_text += d
            board_text += f'|{contador}\t'
            board_text += '\n'
            contador -= 1
        print(board_text)
        print('\t------------------------\t')
        print('\t a  b  c  d  e  f  g  h\t')
        
    def start_posicion(self):
        pass