import numpy as np
from PuzzleGeneration import *

class PuzzleNode:
    """Class to represent a node in tree. 
    A node contains the puzzle configuraton,
    distance from root, and list of moves"""
    def __init__(self, puzzle, distance, moves):
        """User-defined constructor for PuzzleNode class"""
        self.puzzle = puzzle
        self.distance = distance
        self.moves = moves

    def getPuzzle(self):
        """Getter for puzzle"""
        return self.puzzle
    
    def getDistance(self):
        """Getter for distance from root"""
        return self.distance

    def getMoves(self):
        """Getter for list of moves"""
        return self.moves
    
    def setMoves(self, newMove):
        """Set for list of moves"""
        self.moves =  newMove

    def getLastMove(self):
        """Getter for last move"""
        return (self.moves)[-1]

    def getCost(self):
        """Returns cost of a node using c(i) = f(i) + g(i)
        where c(i) is cost of node i, f(i) is cost to reach
        node i from root, and g(i) is total of non-empty tile
        that is in wrong place"""
        cost = self.distance
        for i in range(4):
            for j in range(4):
                if i*4+j+1 != self.puzzle[i, j] and self.puzzle[i, j] != 0:
                    cost += 1
        return cost

    def getRowNull(self):
        """Getter for row of empty tile"""
        row0, col0 = np.where(self.puzzle == 0)
        return row0

    def getColNull(self):
        """Getter for column of empty tile"""
        row0, col0 = np.where(self.puzzle == 0)
        return col0

    def addMove(self, lastMove):
        """Add move to list of moves"""
        self.moves.append(lastMove)

    def moveDown(self):
        """Method to move empty tile down"""
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row+1, col]
        self.puzzle[row+1, col] = 0

    def moveRight(self):
        """Method to move empty tile right"""
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row, col+1]
        self.puzzle[row, col+1] = 0

    def moveUp(self):
        """Method to move empty tile up"""
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row-1, col]
        self.puzzle[row-1, col] = 0

    def moveLeft(self):
        """Method to move empty tile left"""
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row, col-1]
        self.puzzle[row, col-1] = 0

    def comparePuzzle(self, matrix):
        """Method to check if puzzle config is the same as matrix
        using binary comparison"""
        return self.puzzle.tobytes() == matrix.tobytes()
    
    def printNode(self):
        print("Puzzle:")
        PrintPuzzle(self.puzzle)
        print(f"Cost: {self.getCost()}")
        print(f"Distance: {self.distance}")
        print(f"Row: {self.getRowNull()} Col: {self.getColNull()}")
        print(f"Moves: {self.moves}")
        print()