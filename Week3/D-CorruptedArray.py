for _ in range(int(input())):
    n = int(input())
    m = [int(i) for i in input().split()]
    ch = True
    m_ = max(m)
    m.remove(m_)
    s = sum(m)
    for i in range(n+1):
        if s - m[i] == m_:
            print(' '.join([str(m[x]) for x in range(n+1) if x != i]))
            ch = False
            break
    if ch:
        m_ = max(m)
        m.remove(m_)
        if sum(m) == m_:
            print(' '.join([str(m[x]) for x in range(n) if x != i]))
            ch = False
    if ch:
        print(-1)