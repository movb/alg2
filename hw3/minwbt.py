import math
from collections import defaultdict
import numpy as np

def calcmwbt(weights):
    n=len(weights)

    #dp = defaultdict(float)
    #dp = [[0.0 for i in range(n)] for j in range[n]]
    dp = [x[:] for x in [[0]*n]*n]
    for i in range(0,n):
        dp[i][i] = weights[i]

    for s in range(1,n):
        for i in range(0,n-s):
            minw = 1000
            sumw = 0
            for k in range(i,i+s+1):
                sumw += weights[k]
            for r in range(i,i+s+1):
                sm = 0
                if(i<=r-1): sm += dp[i][r-1]
                if(r+1<=i+s): sm+= dp[r+1][i+s]
                if sm < minw:
                    minw = sm
            dp[i][i+s] = sumw + minw
    
    for i in range(n):
        print dp[i][:]
    return dp[0][n-1]

weights = [0.05,0.4,0.08,0.04,0.1,0.1,0.23]

print calcmwbt(weights)
