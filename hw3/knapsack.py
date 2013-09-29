#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    capacity = int(firstLine[0])
    items = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = []
    taken = taken + [0]*(items - len(taken))

    dp = defaultdict(int)

    for i in range(0,capacity+1):
        dp[(0,i)] = 0

    for i in range(0, items):
        for j in range(0,capacity+1):
            if (j-weights[i])>=0:
                dp[(i+1,j)] = max( dp[(i,j)], dp[(i,j-weights[i])]+values[i])
            else:
                dp[(i+1,j)] = dp[(i,j)]
    
    value = dp[(items,capacity)]
    cur_capacity = capacity

    for i in reversed(range(0,items)):
        if dp[(i+1,cur_capacity)] == dp[(i,cur_capacity)]:
            taken[i] = 0
        else:
            taken[i] = 1
            cur_capacity -= weights[i]

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(1) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

