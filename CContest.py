

for _ in range (int(input())):
  n = int(input())

  if n == 2:
    print(-1)
    continue

  a = [[0 for i in range (n)] for j in range (n)]
  c =- 1

  for i in range (n):
    for j in range (n):
      c += 2
      if c > n * n:
        c = 2
        a[i][j] = c
        print(*a[i])