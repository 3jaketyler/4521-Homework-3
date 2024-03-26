# The program in this file is the individual work of Jake Tyler

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
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

    print(recList)
    print(boundBox)