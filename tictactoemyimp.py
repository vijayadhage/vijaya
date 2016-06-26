''' Tic Tac toe game
Author: Annapoornima Koppad
Date:17-May-2016'''

inputmatrix=['0' for i in range(9)]

def checkdiagonal():
	return diagonalval

def checkrows():
	return rowval
    

def computergenintloc():
        loc=1
	return loc

def printtictactoe(inputmatrix):
    print "\t**********Tic Tac Toe**********"
    print "\t-------------------------------"
    i=0
    while i<9:
	j,k,l=i+1,i+2,i+3
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
	j,k,l=i+1,i+2,i+3
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
        j,k,l=i+1,i+2,i+3
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],j,inputmatrix[j],k,inputmatrix[k],l)
        i+=3
        print "\t-------------------------------"
        return

print "This is the default tictactoe board, the computer takes 0 as its representation"
printtictactoe(inputmatrix)

firstplayer=raw_input("Enter 1 if you want to play first : ")

if firstplayer=='1':
	userrep=raw_input("Print your representation: ")
	while userrep=='0':
		print "the computer is representated by 0, please choose anything else apart from 0"
	        userrep=raw_input("Print your representation: ")

	userenterplace=int(raw_input("enter where you want enter your value :"))
	while userenterplace<9:
    		inputmatrix[userenterplace-1]=userrep
		printtictactoe(inputmatrix)
        	genloc=computergenintloc()
		inputmatrix[genloc]='0'
		print "the computer's move is here"
		printtictactoe(inputmatrix)
	        userenterplace=int(raw_input("enter where you want to enter value :"))

	inputmatrix[userenterplace-1]=userrep
	printtictactoe(inputmatrix)
else:
    print "please enter 1"
