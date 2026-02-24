x=0
for _ in range(int(input())):
    L=list(input())
    L.remove("X")
    if "".join(L)=="++":
        x+=1
    else:
        x-=1
print(x)





# Codeforces

# Exercise : 282A-Bit++

# Difficulty : 800