import sys
n = int(sys.stdin.readline())
for i in range(0,n) :
    for j in range(n-i) :
        print("*", end=" ")
    print()