matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
print(matrix)
for i in matrix:
    print(f'i vale {i}')   
    print(matrix.index(i))
    for u in i:
        if u==1:
            print(f'u vale {u}')