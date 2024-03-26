# The program in this file is the individual work of Jake Tyler

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    numRecs = float(input("\nEnter the number of rectangular prisms: "))
    degAcc = int(input("\nEnter your desired degree of accuracy: "))

    recList = []

    print("\nEnter x1, y1, z1, x2, y2, and z2 with spaces in between.\n")
    for i in numRecs:
        userInput = input()
        floats = list(map(float, userInput.split()))
        if len(floats) == 6:
            recList.append(floats)
        else:
            print("Enter exactly six numbers.")

    print(recList)