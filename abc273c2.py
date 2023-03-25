
N = int(input())
A = list(map(int, input().split()))
A.sort()

D = [0] * N
t = 0
D[t] = 1
for i in range(N - 2, -1, -1):
  if A[i] == A[i + 1]:
    D[t] += 1
  else:
    t += 1
    D[t] += 1

for d in D:
  print(d)

