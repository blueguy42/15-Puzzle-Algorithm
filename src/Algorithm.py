import numpy as np
from queue import PriorityQueue
from PuzzleNode import *


def Algorithm(Puzzle):
    # Make dict to check if puzzle config has been checked or not
    checkedMatrics = {}
    # Add root puzzle config to checkedMatrics
    checkedMatrics[Puzzle.tobytes()] = True

    # counter to prioritize innermost node
    priority = 0

    # Make prioqueue of nodes to be checked
    # to prioritize cost then innermost node
    q = PriorityQueue()

    # Add root node to queue
    rootNode = PuzzleNode(Puzzle, 0, [0])
    q.put((rootNode.getCost(), priority, rootNode))

    # Counter for raised nodes
    raisedNodes = 1

    # Initialize matrix to check for solution
    solutionMatrix = np.matrix([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])

    foundSolution = False
    while not q.empty() and not foundSolution:
        # Get innermost node with lowest cost
        currentNode = q.get()[2]
        lastMove = currentNode.getLastMove()

        # Check if node puzzle is solution
        if (currentNode.comparePuzzle(solutionMatrix)):
            foundSolution = True
        else:
            # MOVE ENUMERATION
            # 0 NONE    (note. placeholder for first move)
            # 1 UP		// NEXT MOVE DOWN
            # 2 LEFT	// NEXT MOVE RIGHT
            # 3 DOWN	// NEXT MOVE UP
            # 4 RIGHT	// NEXT MOVE LEFT

            # NEXT MOVE DOWN
            if lastMove != 1 and currentNode.getRowNull() < 3:
                # Make new node with move down
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveDown()
                newNode.addMove(3)
                # Add node if puzzle config has not been checked
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))

            # NEXT MOVE RIGHT
            if lastMove != 2 and currentNode.getColNull() < 3:
                # Make new node with move right
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveRight()
                newNode.addMove(4)

                # Add node if puzzle config has not been checked
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))
            
            # NEXT MOVE UP
            if lastMove != 3 and currentNode.getRowNull() > 0:
                # Make new node with move up
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveUp()
                newNode.addMove(1)
                # Add node if puzzle config has not been checked
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))
            
            # NEXT MOVE LEFT
            if lastMove != 4 and currentNode.getColNull() > 0:
                # Make new node with move left
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveLeft()
                newNode.addMove(2)
                # Add node if puzzle config has not been checked
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))

    currentNode.setMoves(currentNode.getMoves()[1::])
    return currentNode, raisedNodes