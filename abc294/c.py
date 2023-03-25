
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
ans_a = []
ans_b = []

for i in range(len(a)):
    while len(b)>0:
        if a[i] > b[0]:
            count += 1
            ans_b.append(count)
            b.pop(0)
        else:
            count += 1
            ans_a.append(count)
            break
    if len(b) == 0:
        count += 1
        ans_a.append(count)
for j in range(len(b)):
    count += 1
    ans_b.append(count)
            
print(ans_a)
print(ans_b)
            


