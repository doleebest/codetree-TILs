import sys
n = int(sys.stdin.readline())
alphabet = 65
for i in range(1,n+1) :
    for j in range(1,i+1) : 
        print(chr(alphabet), end="")
        alphabet+=1
    print()