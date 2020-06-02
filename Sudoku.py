board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
# row by column


def print_board(board):
    ''' board setup'''
    for i, lines in enumerate(board):
        for j in range(9):
            if j == 8:
                print(board[i][j], '''
''', end='')
            if j == 2 or j == 5 and j != 8:
                print(board[i][j], '|', end=' ')
            elif j != 8:
                print(board[i][j], end=' ')
        if i == 2 or i == 5:
            print('- - - - - - - - - - -')


def spot_finder(board):
    ''' This is going to find an empty spot to solve for'''
    for row, y_value in enumerate(board):
        for col, x_value in enumerate(board[row]):
            if (x_value) == (0):
                # print(f'found a zero at {row} {col}')
                return (row, col)          # (y,x)
    # print('Did not FIND A ZERO')
    return (0, 0)


def check(board, number, placement):
    '''checl to see if the new number is valid in the spot'''
    # row check
    # print(f'the x y placement is {placement}')
    for col in range(len(board)):
        if board[placement[0]][col] == number and spot_finder(board) != number:
            return False
            # column check
    for i in range(len(board[0])):
        if board[i][placement[1]] == number and spot_finder(board) != number:
            return False
    '''check the quadrants by checking which quadrant by column and row quad 1 starts ar top left going in decsending order'''
    if spot_finder(board)[1] < 3:
        if spot_finder(board)[0] < 3:
            for x_cord, row in enumerate(board[:3]):
                for y_cord, actual in enumerate(board[:3]):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        elif spot_finder(board)[0] < 6:
            # quad 2
            for x_cord, row in enumerate(board[:3], start=0):
                for y_cord, actual in enumerate(board[3:6], start=3):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        else:
            # quad 3
            for x_cord, row in enumerate(board[:3], start=0):
                for y_cord, actual in enumerate(board[6:], start=6):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
    elif spot_finder(board)[1] < 6:
        if spot_finder(board)[0] < 3:
            for x_cord, row in enumerate(board[3:6], start=3):
                for y_cord, actual in enumerate(board[:3], start=0):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        elif spot_finder(board)[0] < 6:
            # quad 5
            for x_cord, row in enumerate(board[3:6], start=3):
                for y_cord, actual in enumerate(board[3:6], start=3):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        else:
            for x_cord, row in enumerate(board[3:6], start=3):
                for y_cord, actual in enumerate(board[6:], start=6):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
    else:
        # quad 7
        if spot_finder(board)[0] < 3:
            for x_cord, row in enumerate(board[6:], start=6):
                for y_cord, actual in enumerate(board[:3]):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        elif spot_finder(board)[0] < 6:
            # quad 8
            for x_cord, row in enumerate(board[6:], start=6):
                for y_cord, actual in enumerate(board[3:6], start=3):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
        else:
            # quad 9
            for x_cord, row in enumerate(board[6:], start=6):
                for y_cord, actual in enumerate(board[6:], start=6):
                    if board[y_cord][x_cord] == number and spot_finder(board) != number:
                        return False
    return True


first = -1


def Solver(board):
    global first
    first += 1
    x_cord = -1
    y_cord = -1
    x_cord = spot_finder(board)[0] + x_cord
    y_cord = spot_finder(board)[1] + y_cord
    if x_cord == -1 and y_cord == -1 and first != 0:
        # print('x and y are ZERO')
        return True
    # print(f' x_cord is {x_cord} and y_cord is {y_cord}')
    for i in range(1, 10):
        # print(i)
        if check(board, i, (x_cord + 1, y_cord + 1)):
            # global prior_pos
            # prior_pos = spot_finder(board)[0], spot_finder(board)[1]
            board[x_cord + 1][y_cord + 1] = i
            # print(f'successfully changed board at {x_cord},{y_cord} to {i}')
            # print('''
            # ''')
            # print_board(board)
            # print('''
            # ''')
            # print(check(board, i, spot_finder(board)))
            if Solver(board):
                # print("solver condition" + Solver(board))
                return True
            board[x_cord + 1][y_cord + 1] = 0
            # print(f"board value at {x_cord}, {y_cord} is now {board[x_cord][y_cord]}")
            # print_board(board)
            # return False

    return False


def all(b):
    '''if you import this class into another file you can run this function and it will do everything'''
    Solver(b)
    print_board(b)

