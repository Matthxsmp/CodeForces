import sys
input = sys.stdin.readline
def main():
    A, B, C = map(int,input().strip().split())
    D = 0
    
    for i in range (C):
        D += A * (i+1)
    
    B -= D
    if B < 0 :
        print(abs(B))
    elif B > 0:
        print(0)
    else :
        print (0)
    
main()





# Codeforces

# Exercise : 546A-Soldier And Bananas

# Difficulty : 800