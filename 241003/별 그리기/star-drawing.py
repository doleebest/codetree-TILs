import sys
n = int(sys.stdin.readline())
for i in range(n) :
    for j in range(2-i) :
        print(" ",end='')
    for k in range(2*i+1):
        print("*",end='')
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for k in range(2*n-2*i-3):
        print("*",end='')
    print()