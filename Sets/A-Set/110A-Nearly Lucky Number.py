import sys
input = sys.stdin.readline

def main():
    A = str(input().strip())
    B = 0
    for i in A:
        if i == "4" or i == "7":
            B+=1
    
    for i in [4, 7]:
        if B == i:
            print("YES")
            return
    print("NO")
            
main()





# Codeforces

# Exercise : 110A-Nearly Lucky Number

# Difficulty : 800