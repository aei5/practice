N, M = map(int,input().split())

ans = []

for i in range(1, N + 1):
    ans.append([0] * (N+1))

for j in range(M):
    X = list(map(int,input().split()))
    for k in range(1, X[0]+1):
        for l in range(1, X[0]+1):
            ans[X[k]][X[l]] +=1

Ans = True

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ans[i][j] == 0
            Ans = False

print(Ans)
