import time
import numpy as np
from Exception import *
from Prerequisites import *
from PuzzleGeneration import *
from PuzzleNode import *
from Algorithm import *

try:
    print("=============================================")
    print("     WELCOME TO AFAN'S 15-PUZZLE SOLVER!")
    print("=============================================")
    print("Made by: 13520023 - Ahmad Alfani Handoyo")
    print("Assume: Empty tile is represented with a 0\n")
    print("Generate starting puzzle position:\n1. Randomly generated puzzle\n2. Input from file")
    choose = int(input("Choose 1 or 2: "))

    # Generate a random puzzle
    if choose == 1:
       Puzzle = GeneratePuzzle()

    # Generate a puzzle from a file
    elif choose == 2:
        filename = input("\nInput filename of puzzle: ")
        testPath = dirname((dirname(abspath(__file__)))) + "/test/"
        Puzzle = OpenPuzzle(testPath, filename)

        # Check if puzzle is valid
        CheckValidPuzzle(Puzzle)
    else:
        raise SelectionError
    # Convert matrix to numpy matrix
    Puzzle = np.matrix(Puzzle)
    startingPuzzle = Puzzle.copy()

    print("\nSTARTING PUZZLE CONFIGURATION:")
    PrintPuzzle(Puzzle)

    # Calculate Kurang(i) for each i tile
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

    print("\nPUZZLE SOLUTION IS REACHABLE!")
    print("Calculating solution...\n")
    solutionNode, raisedNodes = Algorithm(Puzzle)
    timeTaken = time.time() - startTime
    solutionMoves = solutionNode.getMoves()
    
    print(f"SOLUTION FOUND IN {len(solutionMoves)} STEPS!\n")
    print("Show steps to reach solution?")
    print("1. Show all steps at once")
    print("2. Show every 10 steps")
    print("3. Show every 5 steps")
    print("4. Show every step")
    print("5. Don't show")
    
    choose = int(input("Choose 1, 2, 3, 4 or 5: "))
    if 1 <= choose <= 4:
        if choose == 1:
            steps = len(solutionMoves)
        elif choose == 2:
            steps = 10
        elif choose == 3:
            steps = 5
        elif choose == 4:
            steps = 1
        
        print("\n================")
        print("    SOLUTION")
        print("================")
        SolutionPrint = PuzzleNode(startingPuzzle,0,[0])
        moveEnum = ["NONE", "UP", "LEFT", "DOWN", "RIGHT"]
        print("\nSTART")
        PrintPuzzle(SolutionPrint.getPuzzle())
        for i in range(len(solutionMoves)):
            if i % steps == 0 and i != 0:
                input("\nPress enter to continue...")
            currentMove = solutionMoves[i]
            if currentMove == 1:
                SolutionPrint.moveUp()
            elif currentMove == 2:
                SolutionPrint.moveLeft()
            elif currentMove == 3:
                SolutionPrint.moveDown()
            elif currentMove == 4:
                SolutionPrint.moveRight()

            print(f"\nSTEP {i+1}")

            PrintPuzzle(SolutionPrint.getPuzzle())
            print(f"MOVE: {moveEnum[currentMove]}")
    elif choose == 5:
        pass
    else:
        raise SelectionError
    
    print(f"\nAlgorithm runtime: {timeTaken} seconds")
    print(f"Raised nodes: {raisedNodes}")
except ValueError:
    print("\nPlease input a number!")
except SelectionError:
    print("\nPlease input an allowed selection!")
except Shape44Error:
    print("\nPlease input a unique 4x4 puzzle with values 0-15!")
except FileNotFoundError:
    print("\nPuzzle file not found!")
except KeyboardInterrupt:
    print(f"Keyboard Interrupt!")
except NotReachableError:
    print("\nPUZZLE SOLUTION IS NOT REACHABLE!")
    print(f"Algorithm runtime: {time.time() - startTime} seconds")

print("\n==============================================")
print(" THANK YOU FOR USING AFAN'S 15-PUZZLE SOLVER!")
print("==============================================")