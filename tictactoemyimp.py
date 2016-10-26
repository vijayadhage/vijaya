''' Tic Tac toe game
Author: Annapoornima Koppad
Date:17-May-2016'''


#Intialize the variables required to play the game
global inputmatrix, locs, dotscompdata, dotsuserdata, userrep

#The input matrix
inputmatrix=[' ' for i in range(9)]

#locations available for the input matrix. This list gets depleted as and when the game progresses
locs=[i for i in range(9)]

#the row and col lists are used while checking if the games gets completed
#here dotscompdata[0]=row1, dotscompdata[1]=row2, dotscompdata[2]=row3
#IIIy dotscompdata[3]=col1,.....
#dotscompdata[6]=leftdia, dotscompdata[7]=rightdia
dotscompdata=[0 for i in range(8)]
dotsuserdata=[0 for i in range(8)]

#initialize a variable that keeps track of the gamewon status
gamewon=False

#function for checking if the rows have been filled
def checkrowcmplrc(rep):

	#check if any of the rows are filled by the user
        #rows are [0,1,2], [3,4,5],[6,7,8]
	print "checcking row data", dotsuserdata, dotscompdata

	#rowof user are 0,1,2, modify dotsuserdata
	for i in range(3):
		#for first row, j ranges from 0,1,2
		if inputmatrix[i]==inputmatrix=[i+1]
			

        k=0
        for i in range(3):
        	j=0
                while j<3:
			print "ijk", i,j,k, inputmatrix[k]
                	if inputmatrix[k]=='0':
                        	dotscompdata[i]+=1
			elif inputmatrix[k]=='*':
				dotsuserdata[i]+=1
                        k+=1
                        j+=1

	print "final row check", dotsuserdata, dotscompdata

	del k,i,j

#function for checking if the rows have been filled
def checkcolcmplrc(rep):

	#columns are [0,3,6],[1,4,7],[2,5,8]
	print "checking col data", dotsuserdata, dotscompdata
        k=0
        for i in range(3,6):
        	j=0
                while j<3:
                	if inputmatrix[k]=='0':
                        	dotscompdata[i]+=1
			elif inputmatrix[k]=='*':
				dotsuserdata[i]+=1
			k+=3
                        j+=1
                k-=8
	print "final coumn check", dotsuserdata, dotscompdata

	del i,j,k

#function to check for filled diagonals
def checkdiagonalcmplrc(rep):

	#check if the left diagonal is filled
        #left diagonal -->  [0,4,8]
	print "printing data before check diagonals", dotscompdata, dotsuserdata

        for j in range(0,9,4):
		if inputmatrix[j]=='0':
			dotscompdata[6]+=1
        	elif inputmatrix[j]=='*':
                	dotsuserdata[6]+=1

	print "final check", dotsuserdata, dotscompdata

        #check if the right diagonal is filled
        #right diagonal -->  [2,4,6]

        for j in range(2,7,2):
		if inputmatrix[j]=='0':
			dotscompdata[7]+=1
	        elif  inputmatrix[j]=='*':
        		dotsuserdata[7]+=1
	print "cecking di", dotsuserdata, dotscompdata
	del j

#function for generating the computer location in the input matrix
def computergenintloc(rep):
	global dotsuserdata, dotscompdata
	loc=None

	#before  generating the computer generated location, check if there are any locations left
	l=len(locs)
	if l>0:

		#before generating location, check the rows, columns, and diagonals are filled by user by checking dotsuserdata
		maxuserdata=max(dotsuserdata)
		if maxuserdata>=3:
			gamewon=True
		#else if the user has not completed the game, generate location
		else:
			print "available locations",locs
			#generating the location based on user data
			

		#of the above four choices, choose the one location that the user will not win and the computer wins
		# for the time being, I have written the first location
#		print dotscompdata, "printing comp data", locs ,"location data", dotsuserdata
#		x=max(dotsuserdata)
#		print x, "maximum of user data", dotsuserdata
#		if x==0:
#			loc=''
#		else:
		loc=locs[0]

		print loc,"exiting the computer generated location"

	if loc is None:
		loc=''
	print "location value", loc
	return loc

def printtictactoe(inputmatrix):
#This function prints the tictactoe board as and when the computer and the user are playing
	print "\t**********Tic Tac Toe**********"
	print "\t-------------------------------"
	i=0
	print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],i,inputmatrix[i+1],i+1,inputmatrix[i+2],i+2)
        i+=3
        print "\t-------------------------------"
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],i,inputmatrix[i+1],i+1,inputmatrix[i+2],i+2)
        i+=3
        print "\t-------------------------------"
        print "\t|  %s (%d)  |  %s (%d)  |  %s (%d)  |" %(inputmatrix[i],i,inputmatrix[i+1],i+1,inputmatrix[i+2],i+2)
        print "\t-------------------------------"
        return

print "This is the default tictactoe board, the computer takes 0 as its representation"
printtictactoe(inputmatrix)

#user input asking if she/he wants to play first
firstplayer=raw_input("Enter 1 if you want to play first : ")

#entering game if the user chooses
if firstplayer=='1':

	#obtain users representation
	userrep=raw_input("Print your representation: ")

	#if the user gives anything else or the computer representation, prompt to provide the right representation
	while userrep=='0':
		print "the computer is representated by 0, please choose anything else apart from 0"
	        userrep=raw_input("Print your representation: ")

	#prompt the user of the locations available for playing the game
	print "these are the locations that are free", locs

	#obtain user's choice
	userenterplace=int(raw_input("enter where you want enter your value :"))
	if userenterplace in locs:

		#while loop ensures that that user's choice are within the limits of the game
		while len(locs)>0:

			# this temp reduces the iteration value by 1 everytime
			temp=userenterplace

			#enter user's choice into the input matrix
    			inputmatrix[temp]=userrep
			print "usp", userenterplace
	
			#once the user enters his value,  then ensure that place is not available for further game
			locs.remove(userenterplace)

			#check if any of the rows  are filled by user
			checkrowcmplrc(userrep)
			# gamewon=funcgamewon()
			print "game won 2", gamewon
			
			#check if any of the columns are filled by user or computer
			checkcolcmplrc(userrep)
#               	gamewon=funcgamewon()
	                print "game won 3", gamewon

			checkdiagonalcmplrc(userrep)
#		gamewon=funcgamewon()
        	        print "game won 4", gamewon

		#print the board for the user's visualization
			print "user filled matrix"
			printtictactoe(inputmatrix)

		#generate a computer value based on the board items
        		genloc=computergenintloc(userrep)
			print "printing gen loc", genloc
			if genloc=='':
				print "Game over! Exiting tic tac toe!!"
				break
			else:
				inputmatrix[genloc]='0'
				locs.remove(genloc)

				#check if any of the rows and columns are filled by computer
				checkrowcmplrc('0')
				#gamewon=funcgamewon()
				print "game won 10", gamewon

				checkcolcmplrc('0')
				#                gamewon=funcgamewon()
				print "game won 13", gamewon

				checkdiagonalcmplrc('0')
#                gamewon=funcgamewon()
				print "game won 14", gamewon
				print "the computer's move is here"
				printtictactoe(inputmatrix)

				print "these are locations that are free", locs
				userenterplace=int(raw_input("enter where you want to enter value :"))
				if userenterplace not in locs:
					print "you entered a inavailable location, enter again"
					userenterplace=int(raw_input("enter where you want to enter value :"))

		inputmatrix[temp]=userrep
		printtictactoe(inputmatrix)
else:
    print "please enter 1"
