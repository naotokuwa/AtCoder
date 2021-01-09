n = int(input())
set_n = set()

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        set_n.add(i)
        set_n.add(n//i)

for i in sorted(list(set_n)):
    print(i)
