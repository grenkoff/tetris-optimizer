from valid_tetrominoes import valid_tetrominoes

def clean(path, flag):
    tetrominoes = clean_tetrominoes(read_tetrominoes(path))
    if not check_tetrominoes(tetrominoes, valid_tetrominoes):
        return
    tetrominoes = replace_alpha(tetrominoes, flag)

    return tetrominoes


def read_tetrominoes(filename):
    tetrominoes = []
    current_tetromino = []
    line_count = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            for char in line:
                if char != '.' and char != '#':
                    return
            line_count += 1

            if line_count % 5 == 0:
                if line == "":
                    continue
                else:
                    return
            else:
                if len(line) != 4:
                    return

            char_list = list(line)
            current_tetromino.append(char_list)

            if len(current_tetromino) == 4:
                tetrominoes.append(current_tetromino)
                current_tetromino = []
    return tetrominoes


def clean_tetrominoes(tetrominoes):
    for _ in range(3):
        # delete empty lines
        for tetromino in tetrominoes:
            for i, line in enumerate(tetromino):
                if line == ['.', '.', '.', '.'] or line == ['.', '.', '.'] or line == ['.', '.'] or line == ['.']:
                    tetromino.pop(i)
        # delete empty colomns from left
        for tetromino in tetrominoes:
            if all(line[0] == '.' for line in tetromino):
                for line in tetromino:
                    line.pop(0)
        # delete empty colomns from right
        for tetromino in tetrominoes:
            if all(line[-1] == '.' for line in tetromino):
                for line in tetromino:
                    line.pop()
    return tetrominoes


def check_tetrominoes(tetrominoes, valid_tetrominoes):
    for tetromino in tetrominoes:
        if str(tetromino) not in valid_tetrominoes:
            return False
    return True


def replace_alpha(tetrominoes, flag):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, tetromino in enumerate(tetrominoes):
        color = valid_tetrominoes[str(tetromino)]
        for line in tetromino:
            for j in range(len(line)):
                if flag:
                    line[j] = line[j].replace('#', color + alphabet[i%26] + '\x1b[0m')
                else:
                    line[j] = line[j].replace('#', alphabet[i%26])

    return tetrominoes
