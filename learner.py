import random

#x represents X on board
#o represents O on board
#- represents Blank space on board


# the key/state in dictionary is shown as indexed

# 012
# 345
# 678

# oxo
# oxx
# ---

# the current player is denoted by 'O' or 'X'
# so the above state is represented as appended string denoting player and the board state
#Eg. 'Ooxooxx---' represents a state mentioned above with O's turn to play

#State appended to an action(index denoting next move) is mapped to expected rewards and stored in Q_table

possibleStates=9+9*8+9*8*7/2+9*8*7*6/4+9*8*7*6*5/12+9*8*7*6*5*4/36+9*8*7*6*5*4*3/144+9*8*7*6*5*4*3*2/(24*24)+9*8*7*6*5*4*3*2*1/(24*120)


Q_table= dict()



currentPlayer = 'O'


boardState=[]


def initializeBoard():
    
    for i in range (9):                               
        boardState.append('-')
    
    for i in range (9):
        newKey= currentPlayer + ''.join(boardState) + i
        Q_table[newKey]= 0
   

    
def Play(currentPlayer):
    
    
    if finalState()=='o' or finalState()=='x' or finalState()=='d':
        return 
    
    nextMoveIndex= getNextStrategy(currentPlayer)
    
    if currentPlayer=='O':
        boardState[nextMoveIndex]='o'
    else:
        boardState[nextMoveIndex]='x'
   
    currentPlayer= changePlayer()
    
    Play(currentPlayer)
    
    
def finalState():
    
    if boardState[0]==boardState[1]==boardState[2]:
        return boardState[0]
        
    if boardState[3]==boardState[4]==boardState[5]:
        return boardState[3]
    
    if boardState[6]==boardState[7]==boardState[8]:
        return boardState[6]
    
    if boardState[0]==boardState[4]==boardState[8]:
        return boardState[0]
    
    if boardState[2]==boardState[4]==boardState[6]:
        return boardState[2]
    
    else:
        for i in range(9):
            if boardState[i]=='-':
                return 'not over'   
        return 'd'
    
    
def getNextStrategy(currentPlayer):
    
    return
    
    
def changePlayer(currentPlayer):
    if currentPlayer=='O':
        return 'X'
    else:
        return 'O'
    
    
def chooseNextMove(currentPlayer, currentBoardState):
    
    if currentPlayer=='O':
        return
        #Maximize Q-value
    else:
        return
        #Minimize Q-value
        
    
#for i in range(1000):
    
  #  initializeBoard()
    
  # Play(currentPlayer)
print(possibleStates)
    
