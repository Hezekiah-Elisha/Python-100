#!/usr/bin/python3
def flatten(array):
    arr = []
    for x in range(len(array)):
        for i in range(len(array[x])):
            arr.append(array[x][i])

    return arr


print(flatten([[7, 8], [3, 4]]))
