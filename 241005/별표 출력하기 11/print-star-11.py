import sys
n = int(sys.stdin.readline())
for i in range(2*n+1):
    if i%2==0 :
        for j in range(2*n+1):
            print("*",end=' ')
    else:
        for k in range(2*n+1):
            if k%2==0 :
                print("*",end=' ')
            else : 
                print(" ",end=' ')
    print()