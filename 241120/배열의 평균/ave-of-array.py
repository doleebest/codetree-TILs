arr = [ list(map(int, input().split())) for i in range(2)]

init =0
for i in range(2) :
    for j in range(4) :
        init += arr[i][j]
    print(round(init/4,1),end= " ")
    init =0
print()


for j in range(4) :
    print(round((arr[0][j] + arr[1][j])/2,1),end=" ")
print()

sum=0
for i in range(2) :
    for j in range(4) :
        sum+=arr[i][j]
print(round(sum/8,1))


    