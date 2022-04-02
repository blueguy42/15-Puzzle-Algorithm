# 15-Puzzle Algorithm

Tugas Kecil 3 IF2211 Strategi Algoritma Semester II Tahun 2021/2022

Solving 15-Puzzle Problems with <i>Branch and Bound</i> Algorithm

## Table of Contents
* [General Information](#general-information)
* [Requirement and Installation](#requirement-and-installation)
* [How to Run](#how-to-run)
* [Example Program Usage](#example-program-usage)
* [Disclaimer](#disclaimer)
* [Contact](#contact)

## General Information
This is a simple program in Python to solve a <a href="https://en.wikipedia.org/wiki/15_puzzle">15-Puzzle</a> by using branch and bound algorithm. The branch and bound algorithm is similar to a breadth first search (BFS) algorithm with the notable difference that the next node to be checked has the lowest cost. This cost is a heuristic function that sums up the distance of the node from the starting position plus the total of mismatched tiles. The algorithm stops when a solution is found, where the puzzle configuration matches the solution matrix:
```
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15  -
```

## Requirement and Installation
Python 3 is used to run the program so make sure it is installed. If it is not, download it first <a href="http://www.python.org/downloads/">here.</a>

Make sure ```python``` and ```pip``` is added to the PATH environment variable. If they are not, follow the guides <a href="http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages">here</a> and <a href="http://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command">here</a>.

If you have not installed the module <b>numpy</b> needed to run the program, install it first by using ```pip```.
 Assuming you have cloned this repository (if not, follow the instructions in the next section), you can also install the modules using this command in the root folder of the repository:
```
pip install -r requirements.txt
```

## How to Run
First, clone the repository:
```
git clone https://github.com/blueguy42/15-Puzzle-Algorithm.git
```
Make sure you are currently in the root directory of the repository. Then, to run the program:
```
python src/Main.py
```

## Example Program Usage

Inputting from a file requires the puzzle to be inputted in a format of numbers 1-15 of 4 rows and 4 columns separated by a space, with an empty tile represented by a 0. For example:
```
5 1 7 3
9 2 6 4
10 11 8 12
13 14 0 15
```
The file needs to be in a .txt format and put in the `test` folder. 

Once you run the program, you should be presented with the following print:
```
=============================================
     WELCOME TO AFAN'S 15-PUZZLE SOLVER!
=============================================
Made by: 13520023 - Ahmad Alfani Handoyo
Assume: Empty tile is represented with a 0

Generate starting puzzle position:
1. Randomly generated puzzle
2. Input from file
Choose 1 or 2: _
```
You can choose to generate the starting puzzle position randomly or from a file. For example, choosing to input from a file and choosing the file `solvable1_15.txt.txt`:
```
Choose 1 or 2: 2

Input filename of puzzle: solvable1_15.txt

STARTING PUZZLE CONFIGURATION:
===========
 5  1  7  3
 9  2  6  4
10 11  8 12
13 14  - 15
===========

Kurang(i):
Tile 1: 0
Tile 2: 0
Tile 3: 1
Tile 4: 0
Tile 5: 4
Tile 6: 1
Tile 7: 4
Tile 8: 0
Tile 9: 4
Tile 10: 1
Tile 11: 1
Tile 12: 0
Tile 13: 0
Tile 14: 0
Tile 15: 0
Empty tile: 1

Sum of Kurang(i) + X:
18

PUZZLE SOLUTION IS REACHABLE!
Calculating solution...
```
The program will show the starting position and Kurang(i)+X value used to calculate the solvability of the puzzle. In this instance, the puzzle is solvable and the solution is calculated for some time.
```
SOLUTION FOUND IN 15 STEPS!

Show steps to reach solution?
1. Show all steps at once
2. Show every 10 steps
3. Show every 5 steps
4. Show every step
5. Don't show
Choose 1, 2, 3, 4 or 5: 1
```
Once the solution is calculated, the user can proceed to show the steps required to reach the solution.
```
================
    SOLUTION
================

START
===========
 5  1  7  3
 9  2  6  4
10 11  8 12
13 14  - 15
===========

STEP 1
===========
 5  1  7  3
 9  2  6  4
10 11  8 12
13 14 15  -
===========
MOVE: RIGHT

STEP 2
===========
 5  1  7  3
 9  2  6  4
10 11  8  -
13 14 15 12
===========
MOVE: UP

...

STEP 14
===========
 1  2  3  4
 5  6  7  8
 9 10 11  -
13 14 15 12
===========
MOVE: DOWN

STEP 15
===========
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15  -
===========
MOVE: DOWN

Algorithm runtime: 0.011640787124633789 seconds
Raised nodes: 117

==============================================
 THANK YOU FOR USING AFAN'S 15-PUZZLE SOLVER!
==============================================
```
Et Voilà! The program will show the runtime required to run the algorithm and the number of nodes generated to find the solution.

## Disclaimer
Due to the limited nature of the branch and bound algorithm, it is not recommended to generate the puzzle randomly using the random generator. Try at your own risk!

## Contact
This program was made by Ahmad Alfani Handoyo (13520023).

You can find and contact me via <a href="http://www.linkedin.com/in/ahmad-alfani-handoyo/">LinkedIn</a>, <a href="http://github.com/blueguy42">GitHub</a>, <a href="http://www.instagram.com/afanhandoyo/">Instagram</a>, or <a href="mailto:ahmadalfanihandoyo1@gmail.com">Email</a>
