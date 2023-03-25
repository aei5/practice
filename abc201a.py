a1, a2, a3 = map(int, input().split())
if (abs(a1-a2) == abs(a1-a3)):
    print("Yes")
elif(abs(a2-a1) == abs(a2 - a3)):
    print("Yes")
elif(abs(a3-a1) == abs(a3 - a2)):
    print("Yes")
else:
    print("No")
