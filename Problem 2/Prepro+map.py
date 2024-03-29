# The program in this file is the individual work of Jake Tyler

import sys
import random
import os


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
    with open("data.txt", "r") as r:
        numRecs = int(r.readline().strip())
        degAcc = float(r.readline().strip())
        boundBox = list(map(float, r.readline().strip().split()))
        for i in range(numRecs):
            recList.append(list(map(float, r.readline().strip().split())))

    result = mapper(recList, boundBox)

    if os.path.exists("tmp.txt") and os.path.getsize("tmp.txt") == 0:
        print(str(degAcc))
        for point in boundBox:
            print(point)
    print(result)