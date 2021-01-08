n = int(input())
lis = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i):
        for k in range(j):
            x3 = lis[k][0]
            y3 = lis[k][1]
            x1 = lis[i][0] - x3
            y1 = lis[i][1] - y3
            x2 = lis[j][0] - x3
            y2 = lis[j][1] - y3
            if x1 * y2 == x2 * y1:
                print('Yes')
                exit()
print('No')
           