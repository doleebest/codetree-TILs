import sys
n = int(sys.stdin.readline())
for i in range(n) :
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(n-1,0,-1) :
    for j in range(j):
        print("*", end=' ')
    print()