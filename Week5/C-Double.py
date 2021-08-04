def com(a, b):
  #gfg
  dp = [[0 for k in range(len(b)+1)] for l in range(len(a)+1)]
  res = 0
  for i in range(len(a) + 1):
    for j in range(len(b) + 1):
      if (i == 0 or j == 0):
        dp[i][j] = 0
      elif (a[i-1] == b[j-1]):
        dp[i][j] = dp[i-1][j-1] + 1
        res = max(res, dp[i][j])
      else:
        dp[i][j] = 0
    return res

t  =int(input())
for _ in range(t):
  a = input()
  b = input()
  x = com(a,b)
  print(len(a)+len(b)-2*x)
