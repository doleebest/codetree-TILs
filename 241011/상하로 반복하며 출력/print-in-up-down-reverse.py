n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2!=0 : print(f"{i}",end='')
        else : print(f"{n+1-i}",end='')
    print()