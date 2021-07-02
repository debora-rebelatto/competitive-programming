import sys

def doTheThing( highest, lowest, count ):
  lengthStones = len(stones) - 1
  lastNumber = stones[lengthStones]
  firstNumber = stones[0]

  if lastNumber == highest or lastNumber == lowest:
    stones.pop()
  elif firstNumber == highest or firstNumber == lowest:
    stones.pop(0)
  else:
    stones.pop()

  print(stones)

if __name__ == '__main__':
  # testCases = int(input())
  testCases = 1

  for _ in range(testCases):
    # numberStones = int(input())
    # stones = [int(x) for x in sys.stdin.readline().split(' ')]

    stones = [2, 3, 1, 4]
    stones = [4, 2, 3, 1, 8, 6, 7, 5]

    lowest = min(stones)
    highest = max(stones)


    indexlow = stones.index(min(stones))
    indexhigh = stones.index(max(stones))

    print(lowest)
    print(highest)

    print(indexlow)
    print(indexhigh)

    count = 0

    while (highest in stones) or (lowest in stones):
      doTheThing(highest, lowest, count)
      count += 1

    print(count)