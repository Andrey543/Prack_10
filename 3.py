input=open('input.txt','r')
s=input.read()
s=s.replace('.',' ')
s=s.replace(',',' ')
s=s.replace('?',' ')
s=s.replace('!',' ')
s=s.replace('\n',' ')
s=s.lower()
static={}
while s[len(s)-1]==' ':
    s=s[:len(s)-1]
while s[0]==' ':
    s=s[1:]
s=s+' '
while len(s)>0:
    a=s[0:s.index(' ')]
    print(a)
    if a in static:
        static[a]+=1
    else:
        static[a]=1
    s=s[s.index(' ')+1:]
    while len(s)>0 and s[0]==' ':
        s=s[1:]
print(len(static))
maximum=0
maxim=''
for key in static:
    if static[key]>= maximum:
        maxim=key
        maximum=static[key]
print(maxim, static[maxim])
