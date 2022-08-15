form = input().split('-')

div = []
for i in form:
    count = 0
    plus = i.split('+')
    for j in plus:
        count += int(j)
    div.append(count)

result = div[0]
for i in range(1, len(div)):
    result -= div[i]

print(result)
