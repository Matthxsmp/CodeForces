import sys
input = sys.stdin.readline

def main():
    A = str(input().strip())
    chars=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    A = A.lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("y", "")
    for i in chars:
        for j in A:
            if j == i:
                A = A.replace(j, f".{j}").replace("..",".")
    print(A)
main()





# Codeforces

# Exercise : 118A-String Task

# Difficulty : 1000