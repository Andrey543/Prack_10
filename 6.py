enru=open('en-ru.txt','r')
ruen=open('ru-en.txt','r')
enru1=open('en-ru1.txt','w')
ruen1=open('ru-en1.txt','w')
s=enru.read()
slovarenru={}
while len(s)>1:
    slovarenru[s[:s.index(' - ')]]=s[s.index(' - ')+3:s.index('\n')]
    s=s[s.index('\n')+1:]
s=ruen.read()
slovarruen={}
while len(s)>1:
    slovarruen[s[:s.index(' - ')]]=s[s.index(' - ')+3:s.index('\n')]
    s=s[s.index('\n')+1:]
ruen=open('ru-en.txt','a')
 

