S=[]
P=[]
for _ in range(int(input())):
    F=list(input().strip())
    if len(F)>10:
        S+=[F[0],str(len(F)-2),F[-1]]
        P.append("".join(S))
        S=[]
    else:
        P.append("".join(F))
print('\n'.join(P))





# Codeforces

# Exercise : 71A-Way Too Long Words

# Difficulty : 800