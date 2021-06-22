import sys

def pr( something ):
  sys.stdout.write( str(something) + '\n')

def solve(array):
  w_offset = [x - i for i, x in enumerate(array)]

  print('offset')
  print(w_offset)

  seen_counts = {}
  tot = 0

  for e in w_offset:

    print(e)

    if not e in seen_counts:
      seen_counts[e] = 1
    else:
      tot += seen_counts[e]
      seen_counts[e] += 1
      return tot


if __name__ == '__main__':
  testCases = int(input())
  for _ in range(testCases):

    arrayLength = int(input())

    array = [int(x) for x in sys.stdin.readline().split(' ')]

    print(array)

    cnt = solve(array)

    pr(cnt)