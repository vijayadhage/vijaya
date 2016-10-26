"""Author: Annapoornima Koppad
Tic Tac Toe on matrix form
"""

global forcomprow
global foruserrow
global forcompcol
global forusercol
global forcompdia
global foruserdia
global revcomprow
global revuserrow
global revcompcol
global revusercol
global revcompdia
global revuserdia


forcomprow=[0 for i in range(3)]
foruserrow=[0 for i in range(3)]
forcompcol=[0 for i in range(3)]
forusercol=[0 for i in range(3)]
forcompdia=[0 for i in range(2)]
foruserdia=[0 for i in range(2)]
revcomprow=[0 for i in range(3)]
revuserrow=[0 for i in range(3)]
revcompcol=[0 for i in range(3)]
revusercol=[0 for i in range(3)]
revcompdia=[0 for i in range(2)]
revuserdia=[0 for i in range(2)]





def funcgamewon():
	if 3 in forcomprow or 3 in foruserrow or 3 in forcompcol or 3 in forusercol or 3 in forcompdia or 3 in foruserdia or 3 in revcomprow  or 3 in revuserrow or 3 in revcompcol or 3 in revusercol or 3 in revcompdia or 3 in revuserdia:
		return True
	else:
		return False


def checkrow():
#	comprow=[0 for i in range(3)]
#	userrow=[0 for i in range(3)]
	for i in range(3):
		for j in range(3):
			if inputmatrix[(i,j)]==1:
				forcomprow[i]+=1
			else:
				forcomprow[i]-=1
			if inputmatrix[(i,j)]==2:
				foruserrow[i]+=1
			else:
				foruserrow[i]-=1
        for i in range(2,-1,-1):
                for j in range(2,-1,-1):
                        if inputmatrix[(i,j)]==1:
                                revcomprow[i]+=1
                        else:
                                revcomprow[i]-=1
                        if inputmatrix[(i,j)]==2:
                                revuserrow[i]+=1
                        else:
                                revuserrow[i]-=1

	return

def checkcol():
#	compcol=[0 for i in range(3)]
#	usercol=[0 for i in range(3)]
	for i in range(3):
		for j in range(3):
			if inputmatrix[(j,i)]==1:
				forcompcol[i]+=1
			else:
				forcompcol[i]-=1
			if inputmatrix[(j,i)]==2:
				forusercol[i]+=1
			else:
				forusercol[i]-=1
        for i in range(2,-1,-1):
                for j in range(2,-1,-1):
                        if inputmatrix[(j,i)]==1:
                                revcompcol[i]+=1
                        else:
                                revcompcol[i]-=1
                        if inputmatrix[(j,i)]==2:
                                revusercol[i]+=1
                        else:
                                revusercol[i]-=1
	return

def checkdia():
#	compdia=[0 for i in range(2)]
#	userdia=[0 for i in range(2)]
	#for left diagonal
	for i in range(3):
		if inputmatrix[(i,i)]==1:
			forcompdia[0]+=1
		else:
			forcompdia[0]-=1
		if inputmatrix[(i,i)]==2:
			foruserdia[0]+=1
		else:
			foruserdia[0]-=1

        for i in range(2,-1,-1):
                if inputmatrix[(i,i)]==1:
                        revcompdia[0]+=1
                else:
                        revcompdia[0]-=1
                if inputmatrix[(i,i)]==2:
                        revuserdia[0]+=1
                else:
                        revuserdia[0]-=1

	#for right diagonal
	for i in range(3):
		if inputmatrix[(i,2-i)]==1:
			forcompdia[1]+=1
		else:
			forcompdia[1]-=1
		if inputmatrix[(i,2-i)]==2:
			foruserdia[1]+=1
		else:
			foruserdia[1]-=1
        for i in range(2,-1,-1):
                if inputmatrix[(i,2-i)]==1:
                        forcompdia[1]+=1
                else:
                        forcompdia[1]-=1
                if inputmatrix[(i,2-i)]==2:
                        foruserdia[1]+=1
                else:
                        foruserdia[1]-=1


	return

inputmatrix={(x,y):"" for x in range(3) for y in range(3)}
locs=[x for x in inputmatrix.keys()]

gamewon=False

print "User representation is 2 and computer representation is 1"

news=''
for i in range(3):
	for j in range(3):
		news+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
	news+='\n'
        
print news

while len(locs)>0:
	if gamewon:
		break
	userloc=tuple(map(int,raw_input("Enter the location where you want your move: ").strip().split(',')))
	if userloc in locs:
		inputmatrix[userloc]=2
		x=locs.remove(userloc)
	        checkrow()
        	checkcol()
	        checkdia()
        	gamewon=funcgamewon()
	        if gamewon:
                	break
		news=''
		for i in range(3):
	        	for j in range(3):
				news+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
			news+='\n'

		print news
		#computergeneratedloc()
	else:
		print "wrong entry"
		continue

if 3 in foruserrow or 3 in forusercol or 3 in foruserdia or 3 in revuserrow or 3 in revusercol or 3 in revuserdia:
	print "User won the game"
elif 3 in forcompcol or 3 in forcomprow or 3 in forcompdia or 3 in revcompcol or 3 in revusercol or 3 in revuserdia:
	print "Computer won the game"
finalstr=''
for i in range(3):
	for j in range(3):
		finalstr+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
	finalstr+='\n'
        
print finalstr
