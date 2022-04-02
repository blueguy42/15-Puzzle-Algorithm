import numpy as np

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
