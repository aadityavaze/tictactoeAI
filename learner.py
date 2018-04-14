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

nextMove=0
boardState=[]
for i in range (9):                               
    boardState.append('-')
p=0


def chooseAlternateStartPlayer():
    global p
    if p==0:
        p=1
        return 'x'
    else:
        p=0
        return 'o'

def chooseRandomMove():
    r=[]
    for i in range(9):
        if boardState[i]=='-':
            r.append(i)
    if len(r)>0:
        return r[random.randint(0,len(r)-1)]
    else:
        return -1
    

def initializeBoard(startPlayer):
    
    for i in range (9):                               
        boardState[i]='-'
    
    for move in range (9):
        newKey= startPlayer + ''.join(boardState)
        Q_table[newKey+str(move)]= str(random.randint(-15,15)/100)
    
    return


def learn(trainingSize, startPlayer):
    
    
    currentPlayer= startPlayer
    count = 0
    while(count< trainingSize):
        
        
        nextMove = chooseRandomMove()
        
        if(nextMove==-1):
            initializeBoard(chooseAlternateStartPlayer())
            count+=1
        
        key= currentPlayer + ''.join(boardState) + str(nextMove)
    
        if key not in Q_table:
            
            for move in range (9):
                newKey= currentPlayer + ''.join(boardState)
                Q_table[newKey+ str(move)]= random.randint(-15,15)/100
        
        tempState=boardState
        tempState[nextMove]=currentPlayer
        key= changePlayer(currentPlayer) + ''.join(tempState) + str(nextMove)
    
        if key not in Q_table:
            
            for move in range (9):
                newKey= currentPlayer + ''.join(boardState)
                Q_table[newKey+ str(nextMove)]= random.randint(-15,15)/100
        
        
        
        updateQTable(currentPlayer, nextMove)
    
        if finalState()=='game over':
            initializeBoard(chooseAlternateStartPlayer())
            count+=1
        else:
            showBoard()
            boardState[nextMove]=currentPlayer
            currentPlayer=changePlayer(currentPlayer)
            
        

def updateQTable(player, nextMove):
    
    
    if finalState()=='game over':
        expected = returnReward()
    else:
        
        if player=='x':
            expected = float(returnReward()) + (discount * minQ(player, nextMove))
        else:
            expected = float(returnReward()) + (discount * maxQ(player, nextMove))
        
    change = learningRate * (expected - float(Q_table[player + ''.join(boardState)+ str(nextMove)]))
            
    Q_table[player + ''.join(boardState)+str(nextMove)] = str(float(Q_table[player + ''.join(boardState)+str(nextMove)]) + change)
    
    
def minQ(currentPlayer, move):
    
    tempState=boardState
    tempState[move]=currentPlayer
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMin=10
        
        if key+str(i) in Q_table:
            
            if tempMin>Q_table[key + str(i)]:
                tempMin=Q_table[key + str(i)]
         
    return tempMin
    
def maxQ(currentPlayer, move):
    
    tempState=boardState
    tempState[move]=currentPlayer
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMax=10
        
        if key+str(i) in Q_table:
            
            if tempMax>float(Q_table[key + str(i)]):
                tempMax=float(Q_table[key + str(i)])
         
    return tempMax
           
    
def finalState():
    
    if (boardState[0]==boardState[1]==boardState[2]=='x') or (boardState[0]==boardState[1]==boardState[2]=='o'):
        return boardState[0]
        
    if (boardState[3]==boardState[4]==boardState[5]=='x') or (boardState[3]==boardState[4]==boardState[5]=='o'):
        return boardState[3]
    
    if (boardState[6]==boardState[7]==boardState[8]=='x') or (boardState[6]==boardState[7]==boardState[8]=='o'):
        return boardState[6]
    
    if (boardState[0]==boardState[4]==boardState[8]=='x') or (boardState[0]==boardState[4]==boardState[8]=='o'):
        return boardState[0]
    
    if (boardState[2]==boardState[4]==boardState[6]=='x') or (boardState[2]==boardState[4]==boardState[6]=='o'):
        return boardState[2]
    
    else:
        for i in range(9):
            if boardState[i]=='-':
                return 'not over'   
        return 'd'
    
    

def returnReward():
    
    if finalState()=='x':
        return float(1.0)
    if finalState()=='o':
        return float(-1.0)
    if finalState()=='not over' or finalState()=='d':
        return float(0.0)

    
def changePlayer(player):
    if player=='o':
        return 'x'
    else:
        return 'o'
    
def showBoard():
    print(boardState[0]+boardState[1]+boardState[2])
    print(boardState[3]+boardState[4]+boardState[5])
    print(boardState[6]+boardState[7]+boardState[8])
    print('\n')
    return 


initializeBoard('o')
learn(100,'o')

    
