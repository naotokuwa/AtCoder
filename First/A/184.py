#my code
lis = []
for i in range(2):
    lis_1 = list(map(int, input().split()))
    lis.append(lis_1)

print(lis[0][0]* lis[1][1] - lis[0][1] * lis[1][0])

#sample code
a, b = map(int, input().split())
c,d = map(int, input().split())
print(a*d - b*c)