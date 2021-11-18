# square = input('Enter:\n')
#
# val = (((ord(square[0]) - 65) * 8) + int(square[1]))
#
# print(val)
import math
#
# def make_board():
board = []

# NOTE FOR NEXT TIME: EVERY OTHER PIECE???

for i in range(64):
    row_ind = math.floor(i / 8)

    if row_ind < 3:
        piece_letter = "b"
    else:
        piece_letter = "w"

    if row_ind != 3 and row_ind != 4:
        if row_ind < 4:
            if row_ind % 2 == 0:
                if i % 2 == 0:
                    board.append(piece_letter)
                else:
                    board.append(" ")
            else:
                if i % 2 == 0:
                    board.append(" ")
                else:
                    board.append(piece_letter)
        else:
            if row_ind % 2 == 0:
                if i % 2 == 0:
                    board.append(" ")
                else:
                    board.append(piece_letter)
            else:
                if i % 2 == 0:
                    board.append(piece_letter)
                else:
                    board.append(" ")
    # elif row_ind > 4:
    #     if row_ind % 2 == 0:
    #         if i % 2 == 0:
    #             board.append("w")
    #         else:
    #             board.append(" ")
    #     else:
    #         if i % 2 == 0:
    #             board.append(" ")
    #         else:
    #             board.append("w")
    else:
        board.append(" ")

# # placing black and white pieces
# for i in range(2):
#     if i == 0:
#         piece_letter = "b"
#     else:
#         piece_letter = "w"
#     for j in range((i*40),(i*40)+24,2):
#         board[j] = piece_letter
#
# print(board)

# def print_board(self):
board_letter = 65 # ASCII code for a capital letter A

for row in [board[i*8:(i+1) * 8] for i in range(8)]:
    print(f'{chr(board_letter)} | ' + ' | '.join(row) + ' |') # denotes each row with a letter in alphabetical order
    board_letter = board_letter + 1
print('    1   2   3   4   5   6   7   8   ') # denotes each column with a number
