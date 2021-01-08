N = int(input())
divs = set()

x = 1
while x ** 2 <= N:
    if N % x == 0:
        divs.add(x)
        divs.add(N // x)
    x += 1

ans = list(divs)
ans.sort()
for x in ans:
    print(x)