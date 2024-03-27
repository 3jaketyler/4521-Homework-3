# The program in this file is the individual work of Jake Tyler

import sys

if __name__ == "__main__":
    mapperOut = []
    boundBox = []

    degAcc = input().strip()
    for i in range(6):
        boundBox.append(input().strip())

    while True:
        result = input().strip()
        if result == "":
            break
        mapperOut.append(result)

    allIn = sum(mapperOut.get() for result in mapperOut)
    allGen = 200 * 10000
    boundVol = (boundBox[3] - boundBox[0]) * (boundBox[4] - boundBox[1]) * (boundBox[5] - boundBox[2])
    ratio = allIn / allGen
    volume = ratio * boundVol
    volAcc = round(volume / degAcc) * degAcc
    volFor = "{:.3f}".format(volAcc)
    print("The volume is: " + str(volFor))