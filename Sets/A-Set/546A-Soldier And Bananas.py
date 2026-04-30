import sys
input = sys.stdin.readline
def main():
    b, i, q = map(int,input().strip().split())
    r=b
    while q>0:
        q-=1
        i-=b
        b+=r
    print(abs(i))
main()





# Codeforces

# Exercise : 546A-Soldier And Bananas

# Difficulty : 800