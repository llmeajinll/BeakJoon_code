total = int(input())
n = int(input())
sum = 0
for i in range(n):
    price, num = map(int, input().split())
    sum += price*num

if total==sum:
    print("Yes")
else:
    print("No")