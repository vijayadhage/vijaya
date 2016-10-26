from datetime import datetime
from operator import itemgetter

u=[]

f=open("sparkdata.txt", "r")
for i in f:
	s=i.strip().split()
	t= s[1]+' '+s[2]
	date_object=datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
	u.append((date_object,s[0],s[3]))

f.close()

x=sorted(u,key=itemgetter(1))
for i in x:
	print i[0],i[1],i[2]
