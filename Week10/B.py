f=str.replace
for s in[*open(0)][2::2]:
 if{*s}=={*'?\n'}:s='R'+s[1:]
 while'?'in s:s=f(f(f(f(s,'R?','RB'),'B?','BR'),'?R','BR'),'?B','RB')
 print(s)