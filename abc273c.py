
N = int(input())
A = list(map(int, input().split()))
d = {} #辞書型使うんだ


for i in range(N):
    d.setdefault(A[i], 0)
    d[A[i]] += 1 #キーそれぞれがでた瞬間に+1

li = sorted(d.items(), reverse = True) #たぶんキーでsort

for j in li:
    print(j[1])
for k in range(N-len(li)):
    print(0)



