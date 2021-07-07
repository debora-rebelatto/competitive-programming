t = int(input())
for _ in range(t):
  n = int(input())
  lis = input().split()
  counter = 0
  for x in range(1,n):
    if lis[x] == lis[0]:
      counter += 1
    else:
      ans = x
  if counter == 0:
    print(0 + 1)
  else:
    print(ans + 1)