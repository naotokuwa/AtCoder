#my code
n = int(input())

if n < 2:
    result = 0
else:
    whole = 10 ** n
    minus = 2 * 9 ** n - 8 ** n
    result = (whole - minus) % (10**9 + 7)
print(result)

#sample code
MOD = 10 ** 9 + 7
N = int(input())

ans = pow(10, N, MOD)
ans -= 2 * pow(9, N, MOD)
ans += pow(8, N, MOD)
ans %= MOD

print(ans)