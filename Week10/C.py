for s in[*open(0)][2::2]:s='0'+s[::2]+'1';n=len(s)-1;i=s.find('01')+1;print(*([-1],[*range(1,i),n,*range(i,n)])[i>0])
