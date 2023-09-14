from argparse import ArgumentParser

from clean import clean
from solve import solve
from display import display

def main():
    parser = ArgumentParser()

    parser.usage = 'python3 main.py [FILE] [--color]'
    parser.add_argument('filename', help='Filename stored tetrominoes')
    parser.add_argument('--color', '-color',
                        help='Paints the figures in the colors of the classic game Tetris', 
                        action='store_true')

    args = parser.parse_args()

    filename = "samples/" + args.filename

    valid_tetrominoes = clean(filename, args.color)
    solution = solve(valid_tetrominoes)
    display(solution)


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print('File not exist')
    except (TypeError, IndexError):
        print('ERROR')
