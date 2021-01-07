#sample code
a,b = map(int, input().split())
c,d = map(int, input().split())

#Start from the origin.
c = abs(c - a)
d = abs(d - b)
res = abs(c - d)

#The start point is equal to the end point.
if c == 0 and d == 0:
    ans = 0


elif c + d <= 3 or res == 0:
    ans = 1

elif res % 2 == 0 or res <= 3 or c + d <= 6:
    ans = 2

else:
    ans = 3

print(ans)


