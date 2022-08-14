N = int(input())
count = [[0]*10 for _ in range(N)]
count[0] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1, N):
    for j in range(10):
        if j == 0:
            count[i][j] = count[i-1][1]
        elif j == 9:
            count[i][j] = count[i-1][8]
        else:
            count[i][j] = count[i-1][j-1] + count[i-1][j+1]

print(sum(count[N-1])%1000000000)