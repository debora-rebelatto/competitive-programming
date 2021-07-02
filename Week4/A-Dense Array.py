from math import *

for i in range(int(input())):
  arrLen = int(input())

  arr = list(map(int, input().split()))

  c = 0

  for i in range(1, arrLen):
    x = max(arr[i], arr[i - 1])
    y = min(arr[i], arr[i - 1])
    while((x / y) > 2):
      y = y * 2
      c += 1
  print(c)
