import math

num = int(input())
# print(num>>1)
dp = [1 for i in range(num + 1)]
dp[0] = 0
for i in range(1, num + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[((i - 1) >> 1) + 1]

ans = "["
for i in dp:
    ans += str(i) + ","
ans = ans[:-1]
ans += "]"
print(ans)
