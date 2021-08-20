for s in[*open(0)][1:]:a,b,c=map(int,s.split());d=abs(a-b);print((c+d,c-d,-1)[min(2,-1--c//d)]if a<=2*d>=b else-1)
