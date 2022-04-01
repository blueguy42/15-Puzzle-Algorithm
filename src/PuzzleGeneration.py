import random
from Exception import *

def CheckValidPuzzle(puzzle):
    """Check if a puzzle is considered valid"""

    # Check if rows of puzzle are 4
    if len(puzzle) != 4:
        raise Shape44Error
    # Check if length of each row is 4
    for i in range(4):
        if len(puzzle[i]) != 4:
            raise Shape44Error
    # Check if length of unique elements is 16
    if len(list(set(i for j in puzzle for i in j))) != 16:
        raise Shape44Error
    # Check if each element is between 0 and 15
    for i in range(4):
        for j in range(4):
            if not 0 <= puzzle[i][j] <= 15:
                raise Shape44Error


def GeneratePuzzle():
    """Generate a random puzzle"""
    Puzzle = [[0 for j in range(4)] for i in range(4)]
    Elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(4):
        for j in range(4):
            Puzzle[i][j] = random.choice(Elements)
            Elements.remove(Puzzle[i][j])
    return Puzzle


def OpenPuzzle(filename):
    """Open a puzzle from a file"""
    with open('test/'+filename, 'r') as f:
            Puzzle = [[int(num) for num in line.split()] for line in f]
    return Puzzle


def PrintPuzzle(puzzle):
    """Print puzzle with padding for 1 or 2 digits"""
    for i in range(4):
        for j in range(4):
            if puzzle[i, j] < 10:
                print(f" {puzzle[i, j]} ", end="")
            else:
                print(f"{puzzle[i, j]} ", end="")
        print()