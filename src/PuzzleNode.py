import numpy as np
from PuzzleGeneration import *

class PuzzleNode:
    def __init__(self, puzzle, distance, moves):
        self.puzzle = puzzle
        self.distance = distance
        self.moves = moves

    def getPuzzle(self):
        return self.puzzle
    
    def getDistance(self):
        return self.distance

    def getMoves(self):
        return self.moves

    def getLastMove(self):
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
        row0, col0 = np.where(self.puzzle == 0)
        return row0

    def getColNull(self):
        row0, col0 = np.where(self.puzzle == 0)
        return col0

    def addMove(self, lastMove):
        self.moves.append(lastMove)

    def moveDown(self):
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row+1, col]
        self.puzzle[row+1, col] = 0

    def moveRight(self):
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row, col+1]
        self.puzzle[row, col+1] = 0

    def moveUp(self):
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row-1, col]
        self.puzzle[row-1, col] = 0

    def moveLeft(self):
        row = self.getRowNull()
        col = self.getColNull()
        self.puzzle[row, col] = self.puzzle[row, col-1]
        self.puzzle[row, col-1] = 0

    def isSolution(self):
        solution = True
        flattenSolution = np.asarray(self.puzzle).flatten()
        for i in range(len(flattenSolution)-1):
            if flattenSolution[i] != i+1:
                solution = False
                break
        return solution

    def comparePuzzle(self, matrix):
        return self.puzzle.tobytes() == matrix.tobytes()
    
    def printNode(self):
        print("Puzzle:")
        PrintPuzzle(self.puzzle)
        print(f"Cost: {self.getCost()}")
        print(f"Distance: {self.distance}")
        print(f"Row: {self.getRowNull()} Col: {self.getColNull()}")
        print(f"Moves: {self.moves}")
        print()