sure=0
solution=0
for _ in range(int(input())):
    sure=0
    a=input().split()
    for i in a:
        if i=="1":
            sure+=1
        if sure>=2:
            solution+=1
            sure=0
print(solution)