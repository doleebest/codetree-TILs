import sys
n = int(input())
gpa = map(float, sys.stdin.readline().split())
sum=0
for i in gpa :
    sum += i
total = sum/n
print(round(total,1))
if total >= 4.0 : print("Perfect")
elif total >=3.0 : print("Good")
else : print("Poor")