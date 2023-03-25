
h, w = map(int, input().split())
a = []
for i in range(h):
    lst = list(map(int, input().split()))
    a.append(lst)

alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(h):
    for j in range(w):
        if a[i][j] == 0:
            a[i][j] = "."
        else:a[i][j] = alfa[a[i][j]-1]

for i in range(h):
    print("".join(a[i]))
