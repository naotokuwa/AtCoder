n = int(input())
lis = list(map(int, input().split()))
ans = 0

for i in range(n-1):
    if lis[i] > lis[i+1]:
        dif = lis[i] - lis[i+1]
        ans += dif
        lis[i+1] += dif

print(ans)