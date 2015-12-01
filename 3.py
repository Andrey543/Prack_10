input=open('LICENSE.txt','r')
s=input.read()
s=s.lower()
static={}
s=s.rstrip()
s=s.lstrip()
s=s.split()
for i in range(len(s)):
    if s[i] in static:
        static[s[i]]+=1
    else:
        static[s[i]]=1
print(len(static))
maximum=0
maxim=''
for key in static:
    if static[key]>= maximum:
        maxim=key
        maximum=static[key]
print(maxim, static[maxim])
