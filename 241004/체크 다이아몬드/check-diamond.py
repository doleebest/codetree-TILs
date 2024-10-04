import sys
n = int(sys.stdin.readline())
for i in range(n):
    for j in range(n-1-i):
        print("_",end='')
    for k in range(i+1) :
        print("*",end=' ')
    print()

for i in range(n):
    for j in range(i+1) :
        print("_",end='')
    for k in range(n-1-i):
        print("*",end=' ')
    print()