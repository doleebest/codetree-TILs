import sys
n = int(sys.stdin.readline())
sum=0
for i in range(1,n) :
    if i%2==0 or i%3==0 or i%5==0 : continue
    sum+=1
print(sum)