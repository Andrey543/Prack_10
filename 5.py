input=open('input.txt','r')
output=open('ru-en.txt','w')
s=input.read()
slovar={}
while len(s)>1:
    slovar[s[:s.index(' - ')]]=s[s.index(' - ')+3:s.index('\n')]
    s=s[s.index('\n')+1:]
vyv=[slovar[x]+' - '+x for x in slovar]
vyv=sorted(vyv)
for i in range(len(slovar)):
    print(vyv[i], file=output)
