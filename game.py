"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed
Twitch KylieYing: https://www.twitch.tv/kylieying
Twitter @kylieyying: https://twitter.com/kylieyying
Instagram @kylieyying: https://www.instagram.com/kylieyying/
Website: https://www.kylieying.com
Github: https://www.github.com/kying18
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ
"""

import math
import time
from player import Player2, RandomComputerPlayer, Player1


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        board = [' ' for _ in range(64)]

        # placing black and white pieces
        for i in range(2):
            if i < 1:
                piece_letter = "b"
            piece_letter = "w"
            for j in range((i*40):(i*40)+24):
                if (board[j] % 2) == "1":
                    board[j] = piece_letter

    def print_board(self):
        board_letter = 65 # ASCII code for a capital letter A
        for row in [self.board[i*8:(i+1) * 8] for i in range(8)]:
            print(f'{chr(board_letter)} | ' + ' | '.join(row) + ' |') # denotes each row with a letter in alphabetical order
            board_letter = board_letter + 1
        print('    1   2   3   4   5   6   7   8   ') # denotes each column with a number

    # @staticmethod
    # def print_board_nums():
    #     # 0 | 1 | 2
    #     number_board = [[str(i) for i in range(j*8, (j+1)*8)] for j in range(8)]
    #     for row in number_board:
    #         print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # def winner(self, square, letter):
    #     # check the row
    #     row_ind = math.floor(square / 3)
    #     row = self.board[row_ind*3:(row_ind+1)*3]
    #     # print('row', row)
    #     if all([s == letter for s in row]):
    #         return True
    #     col_ind = square % 3
    #     column = [self.board[col_ind+i*3] for i in range(3)]
    #     # print('col', column)
    #     if all([s == letter for s in column]):
    #         return True
    #     if square % 2 == 0:
    #         diagonal1 = [self.board[i] for i in [0, 4, 8]]
    #         # print('diag1', diagonal1)
    #         if all([s == letter for s in diagonal1]):
    #             return True
    #         diagonal2 = [self.board[i] for i in [2, 4, 6]]
    #         # print('diag2', diagonal2)
    #         if all([s == letter for s in diagonal2]):
    #             return True
    #     return False

    def winner(self, square, letter):
        # check the row
        row_ind = ord(square[0]) - 65
        row = self.board[row_ind*8:(row_ind+1)*8]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square[1]
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        # if all([s == letter for s in column]):
        #     return True
        # if square % 2 == 0:
        #     diagonal1 = [self.board[i] for i in [0, 4, 8]]
        #     # print('diag1', diagonal1)
        #     if all([s == letter for s in diagonal1]):
        #         return True
        #     diagonal2 = [self.board[i] for i in [2, 4, 6]]
        #     # print('diag2', diagonal2)
        #     if all([s == letter for s in diagonal2]):
        #         return True
        # return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_pieces(self, letter):
        if letter == "w":
            return [i for i, x in enumerate(self.board) if x == "w"]
        return [i for i, x in enumerate(self.board) if x == "b"]


def play(game, w_player, b_player, print_game=True):

    game = TicTacToe()
    game.print_board()

    # if print_game:
    #     game.print_board_nums()

    letter = 'w'
    while game.empty_squares(): # TO DO: CHANGE TO MOVES REMAINING
        if letter == 'b':
            square = b_player.get_move(game)
        else:
            square = w_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'b' if letter == 'w' else 'w'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    w_player = Player('w')
    b_player = Player('b')
    t = TicTacToe()
    play(t, w_player, b_player, print_game=True)
