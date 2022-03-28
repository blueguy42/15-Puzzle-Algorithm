import numpy as np
import random
import time
from Exception import *

def PrintPuzzle(puzzle):
    """Print puzzle with padding for 1 or 2 digits"""
    for i in range(4):
        for j in range(4):
            if puzzle[i, j] < 10:
                print(f" {puzzle[i, j]} ", end="")
            else:
                print(f"{puzzle[i, j]} ", end="")
        print()

def CheckValidPuzzle(puzzle):
    """Check if a puzzle is considered valid"""

    # Check if rows of puzzle are 4
    if len(Puzzle) != 4:
        raise Shape44Error
    # Check if length of each row is 4
    for i in range(4):
        if len(Puzzle[i]) != 4:
            raise Shape44Error
    # Check if length of unique elements is 16
    if len(list(set(i for j in Puzzle for i in j))) != 16:
        raise Shape44Error
    # Check if each element is between 0 and 15
    for i in range(4):
        for j in range(4):
            if not 0 <= Puzzle[i][j] <= 15:
                raise Shape44Error


def ArrayKurangI(puzzle):
    """Returns an array of index 0-15 to calculate Kurang(i)
    for each i tile"""
    # Initialize flattened array to iterate easier
    FlattenedPuzzle = (np.asarray(puzzle)).flatten()
    lengthFlattened = len(FlattenedPuzzle)
    KurangI = [0 for i in range(lengthFlattened)]

    # calculte sum of Kurang(i) for each i
    for i in range(lengthFlattened):
        # if i = 0, assume all next elements add up to Kurang(0)
        if FlattenedPuzzle[i] == 0:
            KurangI[FlattenedPuzzle[i]] += lengthFlattened - (i + 1)
        for j in range(i+1, lengthFlattened):
            if FlattenedPuzzle[j] < FlattenedPuzzle[i] and FlattenedPuzzle[j] != 0:
                KurangI[FlattenedPuzzle[i]] += 1
    return KurangI


def PrintTileKurangI(arr):
    """Print Kurang(i) for each i tile"""
    for i in range(1, len(arr)):
        print(f"Tile {i}: {arr[i]}")
    print(f"Empty tile: {arr[0]}")


def KurangIX(puzzle, arrKurangI):
    """calculate X based on 0 position"""
    if (np.where(puzzle == 0)[0] + np.where(puzzle == 0)[1]) % 2 == 1:
        return 1
    else:
        return 0


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


def Cost(puzzle, currentDistance):
    """Returns cost of a node using c(i) = f(i) + g(i)
    where c(i) is cost of node i, f(i) is cost to reach
    node i from root, and g(i) is total of non-empty tile
    that is in wrong place"""
    cost = currentDistance
    for i in range(4):
        for j in range(4):
            if i*4+j+1 != puzzle[i, j] and puzzle[i, j] != 0:
                cost += 1
    return cost

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

    raisedNodes = 1
    queuePuzzle = []
    queueCost = []
    queueDistance = []
    queueMoves = []

    solutionCost = float("inf")
    solutionMoves = []
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
    rootNode = [Puzzle, 0, 0, [0]]
    queuePuzzle.append(Puzzle)
    queueCost.append(0)
    queueDistance.append(0)
    queueMoves.append([0])

    # print(queuePuzzle)
    # print(queueCost)
    # print(queueDistance)
    # print(queueMoves)
    # print()
    # input()

    while queueCost:
        
        currentIndex = queueCost.index(min(queueCost))
        currentPuzzle = queuePuzzle[currentIndex]
        currentCost = queueCost[currentIndex]
        currentDistance = queueDistance[currentIndex]+1
        currentMoves = queueMoves[currentIndex]
        lastMove = currentMoves[-1]

        queuePuzzle.pop(currentIndex)
        queueCost.pop(currentIndex)
        queueDistance.pop(currentIndex)
        queueMoves.pop(currentIndex)

        # Check if node is solution
        solution = True
        flattenSolution = np.asarray(currentPuzzle).flatten()
        for i in range(len(flattenSolution)-1):
            if flattenSolution[i] != i+1:
                solution = False
                break
        if solution:
            # input("LOH EQUAL: ")

            # if not solutionMoves:
            solutionCost = currentCost
            solutionMoves = currentMoves
            print("MASYA ALLAH")
            break
            # else:
            #     if solutionCost > currentCost:
            #         solutionCost = currentCost
            #         solutionMoves = currentMoves
            #         print("TUHANN")
            
            # eliminateIndex = np.where(np.array(queueCost) > currentCost)
            # eliminateIndex = np.array(eliminateIndex)
            # print(eliminateIndex)
            # queuePuzzle = [i for j, i in enumerate(queuePuzzle) if j not in eliminateIndex]
            # queueCost = [i for j, i in enumerate(queueCost) if j not in eliminateIndex]
            # queueDistance = [i for j, i in enumerate(queueDistance) if j not in eliminateIndex]
            # queueMoves = [i for j, i in enumerate(queueMoves) if j not in eliminateIndex]
            # # input("WADIDAW: ")
        else:
        
        

            row0, col0 = np.where(currentPuzzle == 0)

            # NEXT MOVE DOWN
            if lastMove != 1 and row0 < 3:
                newPuzzle = currentPuzzle.copy()
                newPuzzle[row0, col0] = currentPuzzle[row0+1, col0]
                newPuzzle[row0+1, col0] = 0

                queuePuzzle.append(newPuzzle)
                queueCost.append(Cost(newPuzzle, currentDistance))
                queueDistance.append(currentDistance)
                queueMoves.append(currentMoves + [3])

                raisedNodes += 1
            
            # NEXT MOVE RIGHT
            if lastMove != 2 and col0 < 3:
                newPuzzle = currentPuzzle.copy()
                newPuzzle[row0, col0] = currentPuzzle[row0, col0+1]
                newPuzzle[row0, col0+1] = 0
                newNode = [newPuzzle, Cost(newPuzzle, currentDistance), currentDistance, currentMoves + [4]]
                
                queuePuzzle.append(newPuzzle)
                queueCost.append(Cost(newPuzzle, currentDistance))
                queueDistance.append(currentDistance)
                queueMoves.append(currentMoves + [4])

                raisedNodes += 1
            
            # NEXT MOVE UP
            if lastMove != 3 and row0 > 0:
                newPuzzle = currentPuzzle.copy()
                newPuzzle[row0, col0] = currentPuzzle[row0-1, col0]
                newPuzzle[row0-1, col0] = 0
                newNode = [newPuzzle, Cost(newPuzzle, currentDistance), currentDistance, currentMoves + [1]]
                
                queuePuzzle.append(newPuzzle)
                queueCost.append(Cost(newPuzzle, currentDistance))
                queueDistance.append(currentDistance)
                queueMoves.append(currentMoves + [1])

                raisedNodes += 1
            
            # NEXT MOVE LEFT
            if lastMove != 4 and col0 > 0:
                newPuzzle = currentPuzzle.copy()
                newPuzzle[row0, col0] = currentPuzzle[row0, col0-1]
                newPuzzle[row0, col0-1] = 0
                newNode = [newPuzzle, Cost(newPuzzle, currentDistance), currentDistance, currentMoves + [2]]
                
                queuePuzzle.append(newPuzzle)
                queueCost.append(Cost(newPuzzle, currentDistance))
                queueDistance.append(currentDistance)
                queueMoves.append(currentMoves + [2])

                raisedNodes += 1

            # print(queuePuzzle)
            # print(queueCost)
            # print(queueDistance)
            # print(queueMoves)
            # print()

            # input()



    solutionMoves = solutionMoves[1::]
    print(solutionMoves)
    print(f"Time taken: {time.time() - startTime} seconds")
    print(f"Raised nodes: {raisedNodes}")

        

# except ValueError:
#     print("\nPlease input a number!")
except SelectionError:
    print("\nPlease input an allowed selection!")
except Shape44Error:
    print("\nPlease input a unique 4x4 puzzle with values 0-15!")
except FileNotFoundError:
    print("\nPuzzle file not found!")
except NotReachableError:
    print("\nPUZZLE SOLUTION IS NOT REACHABLE!")
    print(f"Time taken: {time.time() - startTime} seconds")