n,m = map(int, input().split())
arr_2d = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        print(arr_2d[i][j], end=" ")
    print()