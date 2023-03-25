N = int(input())
A = list(map(int,input().split()))

even = []
odd  = []
ans = -1

# A集合の奇偶を分ける
for a in A:
    if a % 2 == 0: #aが偶数
        even.append(a)
    else:
        odd.append(a)

even.sort(reverse = True) # 降順
odd.sort(reverse = True)

if len(even) >= 2:
    ans = max(ans, even[0] + even[1]) # ans上書き
if len(odd) >= 2:
    ans = max(ans, odd[0] + odd[1])

print(ans)
