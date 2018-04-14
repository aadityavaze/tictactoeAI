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


Q_table=  {}

discount=0.9
learningRate=0.1
currentPlayer = 'O'


boardState=[]


def initializeBoard():
    
    for i in range (9):                               
        boardState.append('-')
    
    for move in range (9):
        newKey= currentPlayer + ''.join(boardState)
        Q_table[newKey, move]= random.randint(-100,100)/100
    
    return


def learn(trainingSize):
    
    currentState= startState
    
    for i in range(trainingSize):
        
    key= currentPlayer + ''.join(boardState) 
    
    if 
   




    
def Play(currentPlayer):
    
    
    if finalState()=='o':
        print("O Wins!")
        return
        
    if finalState()=='x':
        print("X Wins!")
        return
    
    if finalState()=='d':
        print("Game Draw")
        return
    
    #Choosing next move
    nextMoveIndex= getNextStrategy(currentPlayer)
    
    #Updating the board
    if currentPlayer=='O':
        boardState[nextMoveIndex]='o'
    else:
        boardState[nextMoveIndex]='x'
   
    #Switching Player
    currentPlayer= changePlayer()
    
    #Recursive call 
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
    
    
def minQ():
    
    for i in range(9):
        
        tempMin=1000
        
        if currentPlayer + ''.join(boardState) + i in Q_table:
            
            if tempMin>Q_table[currentPlayer + ''.join(boardState) + i]
            tempMin=Q_table[currentPlayer + ''.join(boardState) + i]
         
        return tempMin
            
def maxQ():
    
    for i in range(9):
        
        tempMax=-1000
        
        if currentPlayer + ''.join(boardState) + i in Q_table:
            
            if tempMax<Q_table[currentPlayer + ''.join(boardState) + i]
            
                tempMin=Q_table[currentPlayer + ''.join(boardState) + i]
         
        return tempMin

def returnReward():
    
    if finalState()=='x':
        
        return 1
    
    if finalState()=='o':
        
        return -1
    if finalState()=='not over':
        
        return 0
    
def getNextStrategy(currentPlayer):
    
    if currentPlayer=='O':
        
        
    return
    
def updateQValues(currentPlayer):
    if finalState()=='game over':
        expected = returnReward()
    else:
        
        if currentPlayer=='X':
            expected = returnReward() + (discount * lowestQvalue(nextKey))
     else
        expected = reward + (discount * highestQvalue(nextKey))
  change = learningRate * (expected - table[stateKey][action])
  table[stateKey][action] += change
    
    

    
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
        
    
for i in range(1000):
    initializeBoard()
    Play(currentPlayer)

    
