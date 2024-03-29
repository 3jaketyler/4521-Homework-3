# The program in this file is the individual work of Jake Tyler

import sys

if __name__ == "__main__":
    mapperOut = []
    boundBox = []

    degAcc = float(input().strip())
    for i in range(6):
        boundBox.append(float(input().strip()))

    for i in range(200):
        result = input().strip()
        if result == "":
            break
        mapperOut.append(float(result))

    allIn = sum(mapperOut)
    allGen = 200 * 10000
    boundVol = (boundBox[3] - boundBox[0]) * (boundBox[4] - boundBox[1]) * (boundBox[5] - boundBox[2])
    ratio = allIn / allGen
    volume = ratio * boundVol
    volAcc = round(volume / degAcc) * degAcc
    volFor = "{:.3f}".format(volAcc)
    print("The volume is: " + str(volFor))