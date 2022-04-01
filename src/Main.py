import time
from queue import PriorityQueue

from Exception import *
from Prerequisites import *
from PuzzleGeneration import *
from PuzzleNode import *

try:
    print("=============================================")
    print("     WELCOME TO AFAN'S 15-PUZZLE SOLVER!")
    print("=============================================")
    print("Assume: Empty tile is represented with a 0\n")
    print("Generate starting puzzle position:\n1. Randomly generated puzzle\n2. Input from file")
    choose = int(input("Choose 1 or 2: "))

    # Generate a random puzzle
    if choose == 1:
       Puzzle = GeneratePuzzle()

    # Generate a puzzle from a file
    elif choose == 2:
        filename = input("\nInput filename of puzzle: ")
        Puzzle = OpenPuzzle(filename)

        # Check if puzzle is valid
        CheckValidPuzzle(Puzzle)
    else:
        raise SelectionError
    # Convert matrix to numpy matrix
    Puzzle = np.matrix(Puzzle)

    print("\nStarting puzzle:")
    PrintPuzzle(Puzzle)

    # Start of program (other than I/O)
    startTime = time.time()
    print("\nKurang(i):")
    KurangArr = ArrayKurangI(Puzzle)
    PrintTileKurangI(KurangArr)    

    print("\nSum of Kurang(i) + X: ")
    Reachability = np.sum(KurangArr) + KurangIX(Puzzle, KurangArr)
    print(Reachability)

    # Reachable if sum of kurang(i) + x is even
    if Reachability % 2 != 0:
        raise NotReachableError
    print("\nPUZZLE SOLUTION IS REACHABLE!\n")

    checkedMatrics = {}
    checkedMatrics[Puzzle.tobytes()] = True

    q = PriorityQueue()
    rootNode = PuzzleNode(Puzzle, 0, [0])
    priority = 0
    raisedNodes = 1
    q.put((rootNode.getCost(), priority, rootNode))

    solutionMatrix = np.matrix([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])

    # Make prioqueue of nodes (matrix, cost, distance from root, previous moves)
    # 0 NONE
    # 1 UP		// NEXT MOVE DOWN
    # 2 LEFT	// NEXT MOVE RIGHT
    # 3 DOWN	// NEXT MOVE UP
    # 4 RIGHT	// NEXT MOVE LEFT

    # list format
    # 0 - Puzzle
    # 1 - Cost
    # 2 - Distance from root
    # 3 - Previous move

    foundSolution = False
    while not q.empty() and not foundSolution:
        currentNode = q.get()[2]
        lastMove = currentNode.getLastMove()

        if (currentNode.comparePuzzle(solutionMatrix)):
            foundSolution = True
        else:
            # NEXT MOVE DOWN
            if lastMove != 1 and currentNode.getRowNull() < 3:
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveDown()
                newNode.addMove(3)
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))

            # NEXT MOVE RIGHT
            if lastMove != 2 and currentNode.getColNull() < 3:
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveRight()
                newNode.addMove(4)
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))
            
            # NEXT MOVE UP
            if lastMove != 3 and currentNode.getRowNull() > 0:
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveUp()
                newNode.addMove(1)
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))
            
            # NEXT MOVE LEFT
            if lastMove != 4 and currentNode.getColNull() > 0:
                newPuzzle = currentNode.getPuzzle().copy()
                newNode = PuzzleNode(newPuzzle, currentNode.getDistance()+1, currentNode.getMoves().copy())
                newNode.moveLeft()
                newNode.addMove(2)
                if newNode.getPuzzle().tobytes() not in checkedMatrics:
                    checkedMatrics[newNode.getPuzzle().tobytes()] = True
                    raisedNodes += 1
                    priority -= 1
                    q.put((newNode.getCost(), priority, newNode))

    currentNode.printNode()
    solutionMoves = currentNode.getMoves()[1::]
    print(solutionMoves)
    print(len(solutionMoves))
    print(f"Time taken: {time.time() - startTime} seconds")
    print(f"Raised nodes: {raisedNodes}")

        

except ValueError:
    print("\nPlease input a number!")
except SelectionError:
    print("\nPlease input an allowed selection!")
except Shape44Error:
    print("\nPlease input a unique 4x4 puzzle with values 0-15!")
except FileNotFoundError:
    print("\nPuzzle file not found!")
except NotReachableError:
    print("\nPUZZLE SOLUTION IS NOT REACHABLE!")
    print(f"Time taken: {time.time() - startTime} seconds")
except KeyboardInterrupt:
    print(f"Raised nodes: {raisedNodes}")
    print(f"Time taken: {time.time() - startTime} seconds")
