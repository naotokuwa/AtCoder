n = int(input())
lis = []
for _ in range(n):
    lis.append(input())
S = set(lis)

for s in S:
    if '!' + s in S:
        print(s)
        exit()
else:
    print('satisfiable')