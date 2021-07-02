import sys

if __name__ == '__main__':
  testCases = int(input())
  for _ in range(testCases):
    count = 0

    array = [int(x) for x in sys.stdin.readline().split(' ')]

    n = array[0]
    l = array[1]
    r = array[2]
    print("n:", n, "l:", l, "r:", r)

    print("Array A: ")

    arrayOfInteger = [int(x) for x in sys.stdin.readline().split(' ')]

    for i in arrayOfInteger:
      for j in arrayOfInteger:
        sum = int(i) + int(j)
        print(i, j)
        print('Sum of i and j', sum)

        if l <= sum and sum <= r:
          count += 1

          print("isbetween")

    print('COUNT:', count)
