n = int(input())
count = 0
i = 0
for i in range(1, (n + 1)):
    if ('7' not in str(i)) and ('7' not in oct(i)):
        count += 1

print(count)

