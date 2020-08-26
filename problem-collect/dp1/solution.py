N = [[5, 3, 5, 4, 4],
     [1, 7, 8, 4, 0],
     [3, 4, 9, 0, 3],
     [3, 4, 10, 0, 3]]


def getResult():
    # dp 缓存值表示选择当前节点的最小绝对值
    dp = [[0 for i in range(len(N[0]))] for j in range(len(N))]
    for j in range(1, len(N[0])):
        for i in range(len(N)):
            min_list = []

            for k in range(len(N)):
                min_list.append(abs(N[i][j] - N[k][j - 1]) + dp[k][j - 1])
            dp[i][j] = min(min_list)

    result = float('inf')
    for i in range(len(N)):
        if dp[i][-1] < result:
            result = dp[i][-1]
    return result


ret = getResult()
print(ret)
