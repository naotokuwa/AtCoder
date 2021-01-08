n = int(input())
mod = n % 3
ans = 0
cnt_1 = 0
cnt_2 = 0
k = len(str(n))

for i in str(n):
    if int(i) % 3 == 1:
        cnt_1 += 1
    elif int(i) % 3 == 2:
        cnt_2 += 1 

if mod == 0:
    ans = 0

elif mod == 1:
    if cnt_1 >= 1 and 1 < k:
        ans = 1
    elif cnt_2 >= 2 and 2 < k:
        ans = 2
    else:
        ans = -1

elif mod == 2:
    if cnt_2 >= 1 and 1 < k:
        ans = 1
    elif cnt_1 >= 2 and 2 < k:
        ans = 2
    else:
        ans = -1

print(ans)
