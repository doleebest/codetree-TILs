n = int(input())
cnt=9
for i in range(n):
    for j in range(n):
        print(cnt,end='')
        if cnt >1 : cnt-=1
        else : cnt = 9
    print()