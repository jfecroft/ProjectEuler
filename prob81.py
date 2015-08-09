"""
python problem 81 solution
"""
from utils import open_file
from collatz import memoize
FILEN = 'p081_matrix.txt'


def format_lines(lines):
    """
    convert lines to tuples of ints
    """
    return tuple([tuple([int(i) for i in line.split(',')]) for line in lines])


@memoize
def minimum_route(matrix):
    """
    return the minimum route to the bottom corner
    """
    min_route = 0
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        if len(matrix[0]) > 1 and len(matrix) > 1:
            min_route += matrix[0][0] + min(
                minimum_route(tuple([i[1:] for i in matrix])),
                minimum_route(matrix[1:]))
        elif len(matrix[0]) > 1:
            min_route += matrix[0][0] + minimum_route(
                tuple([i[1:] for i in matrix]))
        elif len(matrix) > 1:
            min_route += matrix[0][0] + minimum_route(matrix[1:])
    return min_route


def main():
    """
    call from the terminal
    """
    lines = format_lines(open_file(FILEN))
    print minimum_route(lines)

if __name__ == '__main__':
    main()
