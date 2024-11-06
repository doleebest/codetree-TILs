n = int(input())
alphabet = 65
for i in range(1,n+1) :
    for j in range(1,n+1) :
        print(chr(alphabet), end="")
        alphabet+=1
    print()