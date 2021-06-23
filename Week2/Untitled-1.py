import sys

def solve():
  n = int(input())
  i = 0
  j = 0

  # fr(i, 0, n)
  a = [int(x) for x in sys.stdin.readline().split(' ')]

  maxi = * max_element(a, a + n),
  mini = * min_element(a, a + n),

  if (a[i] == maxi):
    maxii = i + 1
  if (a[i] == mini):
    minii = i + 1


  maxii,
  minii

  c = maxii
  d = minii
  if (c < d):
    swap(c, d)

  # cout << min({n - (c - d - 1), n - d + 1, c}) << "\n"

if __name__ == '__main__':

  counti = 0

  testCases = int(input())
  for _ in range(testCases):
    solve()
