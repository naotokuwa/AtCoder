#sample code
from itertools import permutations

N, K = map(int, input().split())
T = []

for _ in range(N):
    s = list(map(int, input().split()))
    T.append(s)

ans = 0

for per in permutations(range(1, N)):
    score = 0
    prev = 0
    for i in range(N-1):
        cur = per[i]
        score += T[prev][cur]
        prev = cur
    score += T[prev][0]

    if score == K:
        ans += 1

print(ans)
