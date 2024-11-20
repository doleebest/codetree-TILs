arr_2d_first = [
    list(map(int,input().split()))
    for _ in range(3)
]
_ = input()
arr_2d_second = [
    list(map(int,input().split()))
    for _ in range(3)
]
for i,j in zip(arr_2d_first, arr_2d_second):
    for k,l in zip(i,j):
        print(k*l, end=" ")
    print()

