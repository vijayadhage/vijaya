import random

xOro = ['X','O']
board = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'']  

print ("Would You Like To Play Versus Another Human Player Or Versus The Computer ?")
vsWho = int(raw_input("Press 1 to play against a human player \nPress 2 to play against the computer \n"))

if vsWho == 1:
    player1 = random.choice(xOro)
    player2 = 0;

    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'

    print "Player 1 is : " + player1 + " and Player 2 is : " + player2
elif vsWho == 2:
    humanPlayer = random.choice(xOro)
    print "You will play as " + humanPlayer

    if humanPlayer == 'X':
        computer = 'O'
    elif humanPlayer == 'O':
        computer = 'X'
elif vsWho != 1 or vsWho != 2:
    print "The number you entered is incorrect"

class Piece(object):
    '''
     Checks to see whether a spot is filled or not
    '''
    def __init__(self):
        pass;

    humanTurn = int(raw_input("Select A Spot You Want To Play On : "))

    if humanTurn < 0 or humanTurn > 8:
        print "There is no such spot"

    if board[humanTurn] != 'X' and board[humanTurn] != 'O':
        board[humanTurn] = 'X'

        while True:
            computerTurn = random.randint(0,8)
            if board[computerTurn] !=  'O' and board[computerTurn] != 'X':
                board[computerTurn] = 'O'
                break
    else:
        print ("This Spot Is Taken Already")


class X(Piece):
    '''
     This is for X, which can either be human or computer
    '''
    def __init__(self, moves):
        self.moves = moves

    def xMovement(self):
        humanTurn = int(raw_input("Select A Spot You Want To Play On : "))
        if humanTurn < 0 or humanTurn > 8:
            print "There is no such spot"
        elif humanTurn == board["X"] or humanTurn == board["O"]:
            print ("This Spot Is Taken Already")

class O(Piece):
    '''
     This is for O, which can either be human or computer
    '''
    def __init__(self, moves):
        self.moves = moves

    def oMovement(self):
        humanTurn = int(raw_input("Select A Spot You Want To Play On : "))
        if humanTurn < 0 or humanTurn > 8:
            print "There is no such spot"
        elif humanTurn == board["X"] or humanTurn == board["O"]:
            print ("This Spot Is Taken Already")

class TicTacToeBoard(object):
    '''
        Creates The Board, and also refreshes everytime a move is made
    '''
    print '========'
    print board[0],'|',board[1],'|',board[2]
    print '========'
    print board[3],'|',board[4],'|',board[5]
    print '========'
    print board[6],'|',board[7],'|',board[8]
    print '========'

def Win():
    '''
    Checks Win Condition for both players
    '''
    if board[0] == 'O' and board[1]  == 'O'  and board[2] == 'O' :
        print "O Wins"
        quit
    elif board[3]  == 'O' and board[4] == 'O' and board[5] == 'O' :
        print "O Wins"
        quit
    elif board[6] == 'O'  and board[7] == 'O'  and board[8] == 'O' :
        print "O Wins"
        quit
    elif board[0] == 'O'  and board[3] == 'O'  and board[6] == 'O' :
        print "O Wins"
        quit
    elif board[1] == 'O'  and board[4] == 'O'  and board[7] == 'O' :
        print "O Wins"
        quit
    elif board[2] == 'O'  and board[5] == 'O'  and board[8] == 'O' :
        print "O Wins"
        quit
    elif board[0] == 'O'  and board[4] == 'O'  and board[8] == 'O' :
        print "O Wins"
        quit
    elif board[2] == 'O'  and board[4] == 'O'  and board[6] == 'O' :
        print "O Wins"
        quit
    elif board[0] == 'X' and board[1]  == 'X'  and board[2] == 'X' :
        print "X Wins"
        quit
    elif board[3]  == 'X' and board[4] == 'X' and board[5] == 'X' :
        print "X Wins"
        quit
    elif board[6] == 'X'  and board[7] == 'X'  and board[8] == 'X' :
        print "X Wins"
        quit
    elif board[0] == 'X'  and board[3] == 'X'  and board[6] == 'X' :
        print "X Wins"
        quit
    elif board[1] == 'X'  and board[4] == 'X'  and board[7] == 'X' :
        print "X Wins"
        quit
    elif board[2] == 'X'  and board[5] == 'X'  and board[8] == 'X' :
        print "X Wins"
        quit
    elif board[0] == 'X'  and board[4] == 'X'  and board[8] == 'X' :
        print "X Wins"
        quit
    elif board[2] == 'X'  and board[4] == 'X'  and board[6] == 'X' :
        print "X Wins"
        quit
