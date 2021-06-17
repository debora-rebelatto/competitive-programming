testCases = int(input())

for _ in range(testCases):
  n = int(input())
  x = len(str(n))
  print(9 * (x - 1) + n // (int('1' * x)))