sam=[1,0,1,0,1,0,1,0,1]

print "checking diagonal values"

for i in (0,4,8):
	if sam[i]==1:
		leftdia=True
	else:
		leftdia=False

for i in (2,4,6):
	if sam[i]==1:
		rightdia=True
	else:
		rightdia=False

print "value of leftdiagonal, rightdiagonl",leftdia, rightdia

