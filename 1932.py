n = int(input())
num=[]
for _ in range(n):
    num.append(list(map(int, input().split())))

k=2
for i in range(1, n):
    for j in range(k):
        # 가장 왼쪽 아래로 갔을 때
        if j == 0:
            num[i][j] = num[i][j] + num[i-1][j]
        # 가장 오른쪽 아래로 갔을 때
        elif i == j:
            num[i][j] = num[i][j] + num[i-1][j-1]
        # 그 사이일 때
        else:
            num[i][j] = max(num[i-1][j-1] + num[i][j], num[i-1][j] + num[i][j])
    k+=1

print(max(num[n-1]))