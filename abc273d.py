
# 入力シーケンス
H, W, rs, rc = map(int, input().split())

N = int(input())
brock = []
for n in range(N):
    ri_ci = list(map(int, input().split()))
    brock.append(ri_ci)

Q = int(input())
direction = []
for q in range(Q):
    di_li = list(map(str, input().split())

# 高橋君の位置処理
for i in range(Q):
    # 行き先読み込み
    if direction[i][0] == "L":
        if rc-1 != 

# 面倒になったのでやめる. おそらくh,wで壁座標をsort
# →二分探索で壁を検索
#   →処理. で, できるソースコード確認したがあってそう

####二分探索###################################

#配列は昇順にソートずみ
def bilower(a,x):
    # a[i]<=x となる最大のiを返す ない時は-1
    if len(a)==0:return -1
    mi=0
    ma=len(a)-1
    if a[0]>x:return -1
    if a[ma]<=x:return ma
    while ma-mi>1:
        mid=(ma+mi)//2
        if a[mid]<=x:mi=mid
        else:ma=mid
    return mi
 
def bihigher(a,x):
    # a[i]>=x となる最小のiを返す ない時は len(a)
    if len(a)==0:return 0
    mi=0
    ma=len(a)-1
    if a[ma]<x:return ma+1
    if a[0]>=x:return 0
    while ma-mi>1:
        mid=(ma+mi)//2
        if a[mid]>=x:ma=mid
        else:mi=mid
    return ma
 
def birange(a,l,r):
    if l>=r:return 0
    r-=1
    #l<=a[i]<r となるiの個数を返す
    left=bihigher(a,l)
    right=bilower(a,r)
    return right-left+1
 
################################################

