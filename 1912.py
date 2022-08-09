n = int(input())
num = list(map(int, input().split()))
size = len(num)

dp = [0]*size
dp[0] = num[0]

for i in range(1, size):
    dp[i] = max(num[i], dp[i-1]+num[i])

print(max(dp))