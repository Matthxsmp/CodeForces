w=int(input())
#print((w/2)%2)
if int(w/2)%2==0:
    if int(w/4)%2==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")