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

# the current player is denoted by 'o' or 'x'
# so the above state is represented as appended string denoting player and the board state
#Eg. 'ooxooxx---' represents a state mentioned above with o's turn to play

#State appended to an action(index denoting next move) is mapped to expected rewards and stored in Q_table


Q_table=  {}

discount=0.9
learningRate=0.1
currentPlayer = 'o'
nextMove=0

boardState=[]



def chooseRandomMove():
    r=[]
    for i in range(9):
        if boardState[i]!='-':
            r.append(i)
    
    return r[random.randint(0,r.length()-1)]
    

def initializeBoard():
    
    for i in range (9):                               
        boardState.append('-')
    
    for move in range (9):
        newKey= currentPlayer + ''.join(boardState)
        Q_table[newKey+ move]= random.randint(-15,15)/100
    
    return


def learn(trainingSize):
    
    count = 0
    while(count< trainingSize):
        
        nextMove = chooseRandomMove()
        
        key= currentPlayer + ''.join(boardState) + nextMove
    
        if key not in Q_table:
            
            for move in range (9):
                newKey= currentPlayer + ''.join(boardState)
                Q_table[newKey+ nextMove]= random.randint(-15,15)/100
        
        tempState=boardState
        tempState[nextMove]=currentPlayer
        key= changePlayer(currentPlayer) + ''.join(tempState) + nextMove
    
        if key not in Q_table:
            
            for move in range (9):
                newKey= currentPlayer + ''.join(boardState)
                Q_table[newKey+ nextMove]= random.randint(-15,15)/100
        
        
        
        updateQTable(currentPlayer, nextMove)
    
        if finalState()=='game over':
            
            initializeBoard()
            count++
        else:
            print("Board State:", boardState)
            boardState[nextMove]=currentPlayer
            currentPlayer=changePlayer(currentPlayer)
            
        

def updateQTable(currentPlayer, nextMove):
    
    
    if finalState()=='game over':
        expected = returnReward()
    else:
        
        if currentPlayer=='x':
            expected = returnReward() + (discount * minQ(nextMove))
        else
            expected = returnReward() + (discount * maxQ(nextMove))
        
    change = learningRate * (expected - Q_table[currentPlayer + ''.join(boardState)+ nextMove])
            
    Q_table[currentPlayer + ''.join(boardState)+nextMove] += change
    
    
def minQ(move):
    
    tempState=boardState
    tempState[move]=currentPlayer
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMin=10
        
        if key+i in Q_table:
            
            if tempMin>Q_table[key + i]
            tempMin=Q_table[key + i]
         
    return tempMin
    
def maxQ(move):
    
    tempState=boardState
    tempState[move]=currentPlayer
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMax=10
        
        if key+i in Q_table:
            
            if tempMax>Q_table[key + i]
            tempMax=Q_table[key + i]
         
    return tempMax
            
    
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
    if currentPlayer=='o':
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
    


    
def changePlayer(player):
    if player=='O':
        return 'X'
    else:
        return 'O'
    
    
def chooseNextMove(currentPlayer, currentBoardState):
    
    if currentPlayer=='o':
        return
        #Maximize Q-value
    else:
        return
        #Minimize Q-value
        
    

initializeBoard()
learn(100)

    
