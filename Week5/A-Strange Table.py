t = int(input())

lis = []
out = []
for i in range(t):
    lis.append([int(j) for j in input().split()])
    count = 0
    if lis[i][2]%lis[i][0] == 0:
        a = lis[i][0]
    else:
        a = lis[i][2]%lis[i][0]
    if lis[i][2]%lis[i][0]==0:
        b = lis[i][2]//lis[i][0]
    else:
        b = lis[i][2]//lis[i][0] +1
    count = (a-1)*lis[i][1]+ b
    out.append(count)
for i in out:
    print(i)


