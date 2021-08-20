R=lambda:map(int,input().split())
t,=R()
exec(t*"n,k=R();a=[0]*n;_,a=zip(*sorted(zip(R(),range(n))));print('YNEOS'[sum(y-x!=1for x,y in zip(a,a[1:]))>k-1::2]);")