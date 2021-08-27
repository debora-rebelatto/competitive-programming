for s in[*open(0)][2::2]:
 r=2**30-1
 for x in s.split():r&=int(x)
 print(r)
