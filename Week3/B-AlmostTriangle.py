import sys

if __name__ == '__main__':
  testCases = int(input())

  for _ in range(testCases):
    rowsAndColumns = int(input())
    arr = []

    for i in range(rowsAndColumns):
      theReadLine = input()
      arr.append(theReadLine)

    count = 0

    for k in arr:
      for i in k:
        if i == "*":
          count += 1

    print(count)




