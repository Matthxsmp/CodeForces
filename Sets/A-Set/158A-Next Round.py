n, k= map(int,input().split())
a=list(map(int,input().split()))
next=0
for i in a:
    if i == 0:
        pass
    elif i >= a[k-1]:
        next+=1
print(next)





# Codeforces

# Exercise : 158A-Next Round

# Difficulty : 800