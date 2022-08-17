N = int(input())
dp = [0, 1, 1, 2, 3]

if N < len(dp):
    print(dp[N])
else:
    for i in range(len(dp), N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp[N])