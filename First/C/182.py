N = list(input())
N = [int(x) for x in N]
k = len(N)
sum_n = sum([int(x) for x in N])
mod = sum_n % 3

cnt_1 = 0
cnt_2 = 0
for n in N:
    if n % 3 == 1:
        cnt_1 += 1
    elif n % 3 == 2:
        cnt_2 += 1

if mod == 0:
    print(0)
    exit()
elif mod == 1:
    if cnt_1 >= 1 and 1 < k:
        print(1)
        exit()
    elif cnt_2 >= 2 and 2 < k:
        print(2)
        exit()
    else:
        print(-1)
        exit()

elif mod == 2:
    if cnt_2 >= 1 and 1 < k:
        print(1)
        exit()
    elif cnt_1 >= 2 and 2 < k:
        print(2)
        exit()
    else:
        print(-1)
        exit()