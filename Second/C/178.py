n = int(input())
MOD = 10 ** 9 + 7

count_whole_mod = 10 ** n % MOD
count_non_0_and_9 = (2 * 9 ** n - 8 ** n) % MOD
result = (count_whole_mod - count_non_0_and_9) % MOD
print(result)
