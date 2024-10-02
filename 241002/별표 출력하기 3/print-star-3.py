import sys
n = int(sys.stdin.readline())
for i in range(n) :
    for j in range(i) : # 공백
        print(" ", end=' ')
    
    for j in range(2*n-2*i-1) : # *
        print("*", end=' ')
    print()