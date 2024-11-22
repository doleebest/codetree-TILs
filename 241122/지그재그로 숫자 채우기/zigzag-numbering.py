import sys
n,m = map(int,sys.stdin.readline().split())
arr = [0 for _ in range(n) for _ in range(m)]

# 열 번호가 짝수인 경우
for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            answer[row][col] = count
            count += 1

# 열 번호가 홀수인 경우
for col in range(m):
    if col % 2 != 0:
        for row in range(n - 1, -1, -1):
            answer[row][col] = count
            count += 1