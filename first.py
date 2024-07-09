# 动态规划
def main(source, target):
    n = len(source)
    m = len(target)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    if dp[n][m] == float('inf'):
        return -1
    else:
        return dp[n][m]

source1 = "abc"
target1 = "abcbc"
result1 = main(source1, target1)
print(f"Example 1: {result1}")  

source2 = "abc"
target2 = "acdbe"
result2 = main(source2, target2)
print(f"Example 2: {result2}")  

source3 = "xyz"
target3 = "xzyxz"
result3 = main(source3, target3)
print(f"Example 3: {result3}")  