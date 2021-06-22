import sys

if __name__ == '__main__':
  testCases = int(input())

  for _ in range(testCases):
    arraySize = int(input())
    array = [int(x) for x in sys.stdin.readline().split(' ')]
