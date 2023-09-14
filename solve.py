def solve(tetrominoes):
    size = board_size(tetrominoes)
    board = get_board(size)
    index = 0
    while not backtrack(board, tetrominoes, index):
        size += 1
        board = get_board(size)
    return board


def board_size(tetrominoes):
    count = len(tetrominoes)
    for i in range(count*4):
        if i*i >= count*4:
            return i


def get_board(size):
    board = []
    line = []
    for _ in range(size):
        for _ in range(size):
            line.append('.')
        board.append(line)
        line = []
    return board


def backtrack(board, tetrominoes, index):
    if index == len(tetrominoes):
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if can_place(board, i, j, tetrominoes[index]):
                place_tetromino(board, i, j, tetrominoes[index])

                if backtrack(board, tetrominoes, index+1):
                    return True
                remove_tetromino(board, i, j, tetrominoes[index])
    return False


def can_place(board, i, j, tetromino):
    for a in range(len(tetromino)):
        for b in range(len(tetromino[0])):
            if tetromino[a][b] != '.':
                if i+a == len(board) or j+b == len(board) or board[i+a][j+b] != '.':
                    return False
    return True


def place_tetromino(board, i, j, tetromino):
    a, b, c = 0, 0, 0
    while a < len(tetromino):
        while b < len(tetromino[0]):
            if tetromino[a][b] != '.':
                c += 1
                board[i+a][j+b] = tetromino[a][b]
                if c == 4: 
                    break
            b += 1
        b = 0
        a += 1


def remove_tetromino(board, i, j, tetromino):
    a, b, c = 0, 0, 0
    while a < len(tetromino):
        while b < len(tetromino[0]):
            if tetromino[a][b] != '.':
                if c == 4:
                    break
                board[i+a][j+b] = '.'
            b += 1
        b = 0
        a += 1
