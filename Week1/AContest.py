testCases = int(input())

for _ in range(testCases):
  doneTasks = int(input())
  tasksIds = input()
  no = False

  for i in range(1, len(tasksIds)):
    if tasksIds[i] in tasksIds[:i] and tasksIds[i] != tasksIds[i - 1]:
      no = True
      break
    else:
      no = False

  if no:
    print('NO')
  else:
    print("YES")
