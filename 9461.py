n = int(input())

def Padvan(N):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N <= len(dp):
        return dp[N-1]
    else:
        for i in range(N-len(dp)):
            dp.append(dp[7+i]+dp[8+i])
            print(dp)
        return dp[N-1]
for i in range(n):
    N = int(input())
    print(Padvan(N))