import time


def fibo1(num):
    if num <= 2:
        return 1
    a, b = (1, 1)
    for i in range(num - 2):
        a, b = b, (a + b)

    return b


# 递归
def fibo2(num):
    if num <= 2:
        return 1
    else:
        return fibo2(num - 1) + fibo2(num - 2)


# 动态规划
def fibo3(num):
    results = list(range(num))
    for i in range(num):
        if i < 2:
            results[i] = 1
        else:
            results[i] = results[i - 1] + results[i - 2]

    return results[-1]


start = time.time()
ret = fibo3(100)
end = time.time()
print(end - start, ret)
