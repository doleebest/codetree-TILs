import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    for j in range(1,n+1) :
        print(f"{i} * {j} = {i*j}")