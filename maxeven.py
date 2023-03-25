N = int(input())
A = list(map(int, input().split()))
ans = 0

for a in A:
    if int(a) % 2 == 0:
        ans += int(a)

if ans % 2 != 0 or ans == 0:
    print(-1)
else:
    print(ans)
