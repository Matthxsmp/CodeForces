import sys
input = sys.stdin.readline
def main():
    A = int(input().strip())
    print (type(A))
    for i in [44, 77, 47, 74, 444, 777, 474, 747, 774, 477, 447, 744, 4, 7]:
        if A % i == 0:
            print("YES")
            return
    print("NO")
main()