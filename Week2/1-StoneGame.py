import sys

testCases = int(input())

for _ in range(testCases):
  numberStones = int(input())

  stones = [int(x) for x in sys.stdin.readline().split(' ')]

  lowest = min(stones)
  highest = max(stones)

  print(lowest)
  print(highest)

  count = 0

  for stone in range(0, numberStones):
    count += 1

    if highest and lowest not in stones:
      break

    lengthStones = len(stones)

    lastNumber = stones[lengthStones - 1]

    firstNumber = stones[0]

    print(lastNumber)
    print(firstNumber)

    if firstNumber < lastNumber:
      stones.pop(0)
    # elif
    #   stones.pop(len(stones))


    print(stones)

  print("COUNT:", count)

