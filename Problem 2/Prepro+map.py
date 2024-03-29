# The program in this file is the individual work of Jake Tyler

import multiprocessing
import sys
import random

def preProcess():
    if len(sys.argv) == 1:
        print("Enter your input:", file=sys.stdout)
        numRecs = int(input("\nEnter the number of rectangular prisms: "))
        degAcc = float(input("\nEnter your desired degree of accuracy: "))

        recList = []

        i = 0

        print("\nEnter x1, y1, z1, x2, y2, and z2 with spaces in between.\n")
        while i < numRecs:
            userInput = input()
            floats = list(map(float, userInput.split()))
            if len(floats) == 6:
                recList.append(floats)
                i += 1
            else:
                print("Enter exactly six numbers.")

        boundBox = []

        min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
        max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')

        for rec in recList:
            min_x = min(min_x, rec[0], rec[3])
            min_y = min(min_y, rec[1], rec[4])
            min_z = min(min_z, rec[2], rec[5])
            max_x = max(max_x, rec[0], rec[3])
            max_y = max(max_y, rec[1], rec[4])
            max_z = max(max_z, rec[2], rec[5])

        boundBox.append(min_x)
        boundBox.append(min_y)
        boundBox.append(min_z)
        boundBox.append(max_x)
        boundBox.append(max_y)
        boundBox.append(max_z)

        with open("data.txt", "w") as w:
            w.write(str(numRecs) + "\n")
            w.write(str(degAcc) + "\n")
            w.write(" ".join(map(str, boundBox)) + "\n")
            for rec in recList:
                w.write(" ".join(map(str, rec)) + "\n")

        sys.stdout = origOut
        sys.stderr = origErr
    else:
        recList = []
        boundBox = []
        numRecs, degAcc = 0

        with open("data.txt", "r") as r:
            numRecs = int(r.readline().strip())
            degAcc = float(r.readline().strip())
            boundBox.append(list(map(float, r.readline().strip().split())))
            for i in range(numRecs):
                recList.append(list(map(float, r.readline().strip().split())))

    return numRecs, degAcc, recList, boundBox

def mapper(recList, boundBox):
    numInPancake = 0
    
    for i in range(10000):
        x = random.uniform(boundBox[0], boundBox[3])
        y = random.uniform(boundBox[1], boundBox[4])
        z = random.uniform(boundBox[2], boundBox[5])

        for rec in recList:
            xIn = (x >= min(rec[0], rec[3])) and (x <= max(rec[0], rec[3]))
            yIn = (y >= min(rec[1], rec[4])) and (y <= max(rec[1], rec[4]))
            zIn = (z >= min(rec[2], rec[5])) and (z <= max(rec[2], rec[5]))
            if xIn and yIn and zIn:
                numInPancake += 1
                break

    return numInPancake

if __name__ == "__main__":
    recList = []
    boundBox = []
    numRecs, degAcc, recList, boundBox = preProcess()

    result = mapper(recList, boundBox)

    if len(sys.argv) == 1:
        print(str(degAcc) + "\n")
        for point in boundBox:
            print(point)
    print(result)