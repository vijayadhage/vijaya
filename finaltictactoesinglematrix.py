''' This program implements a tic tac toe program
Author : Annapoornima Koppad
Date   : 20 August 2016
'''

#Intialize the variables required to play the game
global inputmatrix, locs, dotscompdata, dotsuserdata, userrep
global gamewon

gamewon=False

#The input matrix
inputmatrix=[' ' for i in range(9)]

#locations available for the input matrix. This list gets depleted as and when the game progresses
locs=range(9)

def printtictactoe(inputmatrix):
#This function prints the tictactoe board as and when the computer and the user are playing
    print "\t**********Tic Tac Toe**********"
    print "\t-------------------------------"
    i=0
    while i<9:
        j,k,l=i,i+1,i+2
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
        j,k,l=i,i+1,i+2
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
        j,k,l=i,i+1,i+2
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
        del i,j,k,l
        return

#print function for printing free locations
def printfreelocs():
	print "these are the locations that are free for you, the user to pick: ", 
	for i in locs:
		print i,
	return

#printing the default tictactoe board
print "The default tictactoe board is here"
printtictactoe(inputmatrix)

#printing instructions for the user, you!!!
print "The computer is represented by 0 and you, the player is represented by *, the user always plays first"

#get the value of locations length, to avoid getting it ever time
loclength=len(locs)

while gamewon==False and userenterplace<=9 and loclength<9:

	#prompt the user of the locations that are avialable for choosing
	printfreelocs()

	#obtain user's choice
        userenterloc=int(raw_input("enter where you want enter your value :"))
	#after obtaining the user entered location, check if the location is present in the free locations
	if userenterloc in locs:
		#when the user entered location is free, update it to user's representation and freeze/remove that particular location from locs
		inputmatrix[userenterloc]='*'
		locs.remove(userenterloc)
		#after updating, check if any of the user or computer entered lcoations are filled , if filled, update gamewon
		
	
	else:
		break



