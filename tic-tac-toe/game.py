class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]  # use a single list to store 3x3 board values
        self.current_winner = None  # keep track of the current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + " |")

    @staticmethod
    def print_board_nums():
        pass
        