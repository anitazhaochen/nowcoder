#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 使用二维数组
def getDP(arr, aim):

    dp = [[0 for i in range(-1, aim+1)] for _ in range(len(arr)+1)]

    for i in range(1, len(arr)+1):
        dp[i][0] = arr[i-1]


    for i in range(2,aim+2):
        dp[0][i] = i-1

    for i in range(1,len(arr)+1):
        dp[i][1] = 1

    for i in range(2, aim+2):
        print(i)
        dp[1][i] = (1 if (dp[1][i] % dp[1][0] == 0) else 0)

    for i in range(2, len(arr)+1):
        for j in range(2, aim+2):
            dp[i][j] = (dp[i][j-dp[i][0]] if j-dp[i][0] > 0 else 0 ) + dp[i-1][j]

    for line in dp:
        print(line)

# 使用一维数组优化空间复杂度
def getDP2(arr, aim):
    sum = [0 for i in range(-1, aim+1)]
    sum[0] = 1






def getOneDP(arr, aim):
    dp = [[0 for i in range(-1, aim+1)] for _ in range(len(arr)+1)]
    for i in range(1, len(arr)+1):
        dp[i][0] = arr[i-1]


    for i in range(2,aim+2):
        dp[0][i] = i-1

    for i in range(1,len(arr)+1):
        dp[i][1] = 1

    for i in range(2,aim+2):
        dp[1][i] = 0 if dp[1][0]-dp[0][i] < 0  else dp[1][i-1-dp[0][i]]

    for i in range(2, len(arr)+1):
        for j in range(2,aim+1):
            if dp[i][j] - dp[i][0]>=0:
                dp[i][j] = dp[i][j-dp[i][0]]
            else:
                dp[i][j] = dp[i-1][j]

    #for i in range(2, len(arr)+1):
    #    for j in range(2, aim+2):
    #        one = 1 if j-1 == dp[i][0] else 0
    #        select = dp[i-1][dp[i][j]-dp[i][0]] if dp[i][j] - dp[i][0] >=0 else 0
    #        dp[i][j] += dp[i-1][j]


    for line in dp:
        print(line)





if __name__ == "__main__":
    getDP([1,2,3], 10)
    #getOneDP([1,2,3], 10)
