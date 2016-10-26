"""Author: Annapoornima Koppad
"""

global inputmatrix
global compdata
global userdata
global gamewon

from compiler.ast import flatten

compdata=[[False for i in range(3)], [False for i in range(3)], [False for i in range(2)]]
userdata=[[False for i in range(3)], [False for i in range(3)], [False for i in range(2)]]
gamewon=[False, [],[]]

inputmatrix={(x,y):0 for x in range(3) for y in range(3)}
locs=[(x,y) for x in range(3) for y in range(3)]

def checkrow():
        compdata[0]=[inputmatrix[(i,0)]==inputmatrix[(i,1)]==inputmatrix[(i,2)]==2 for i in range(3)]
	userdata[0]=[inputmatrix[(i,0)]==inputmatrix[(i,1)]==inputmatrix[(i,2)]==1 for i in range(3)]
        return

def checkcol():
	compdata[1]=[inputmatrix[(0,i)]==inputmatrix[(1,i)]==inputmatrix[(2,i)]==2 for i in range(3)]
	userdata[1]=[inputmatrix[(0,i)]==inputmatrix[(1,i)]==inputmatrix[(2,i)]==1 for i in range(3)]
        return

def checkdia():
	#left diagonal
	compdata[2][0]=inputmatrix[(0,0)]==inputmatrix[(1,1)]==inputmatrix[(2,2)]==2
	userdata[2][0]=inputmatrix[(0,0)]==inputmatrix[(1,1)]==inputmatrix[(2,2)]==1

	#right diagonal
	compdata[2][1]=inputmatrix[(0,2)]==inputmatrix[(1,1)]==inputmatrix[(2,0)]==2
	userdata[2][1]=inputmatrix[(0,2)]==inputmatrix[(1,1)]==inputmatrix[(2,0)]==1
        return

def computergenloc():
	if inputmatrix[(1,1)]==0:
		comploc=(1,1)
	else:
		if len(locs)>0:
		#look for locs that are free
			comploc=locs[0]
		else:
			comploc=''
	
	return comploc

def funcgamewon():
	flattenedcompdata=flatten(compdata)
	flatteneduserdata=flatten(userdata)
	if True in flattenedcompdata or True in flatteneduserdata:
		gamewon[0]=True
		gamewon[1]=flatteneduserdata
		gamewon[2]=flattenedcompdata
        return gamewon


news=''
for i in range(3):
        for j in range(3):
                news+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
        news+='\n'

print news

print "User is represented by 1 and the computer is represented by 2"

while len(locs)>0:
        userloc=tuple(map(int,raw_input("Enter the location where you want your move: ").strip().split(',')))
        if userloc in locs:
                inputmatrix[userloc]=1
                x=locs.remove(userloc)
                checkrow()
                checkcol()
                checkdia()
                gamewon=funcgamewon()
                if gamewon[0]:
                        break
		#computer location generation
		comploc=computergenloc()
		if comploc=='':
			print "no more locations available"
			break
		inputmatrix[comploc]=2
		x=locs.remove(comploc)
		checkrow()
                checkcol()
                checkdia()
                gamewon=funcgamewon()
                if gamewon[0]:
                        break

                news=''
                for i in range(3):
                        for j in range(3):
                                news+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
                        news+='\n'

                print news
        else:
                print "wrong entry"
                continue

finalstr=''

for i in range(3):
        for j in range(3):
                finalstr+='('+str(i)+','+str(j)+') : '+str(inputmatrix[(i,j)])+'\t'
        finalstr+='\n'

print finalstr

if gamewon[0]: 
        if True in gamewon[1]:
                print "Game won by user"
        elif True in gamewon[2]:
                print "game won by computer"
        else:
                "Game over!!! Start again"


