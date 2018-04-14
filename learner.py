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

#initialize Board with '-' in all places
def initializeBoard():
    
    for i in range (9):                               
        boardState[i]='-'
    
    return

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
    



def initializeQValues():
    
    for move in range (9):
        newKeyo= 'o---------'
        newKeyx= 'x---------'
        Q_table[newKeyo+str(move)]= str(random.randint(-15,15)/100)
        Q_table[newKeyx+str(move)]= str(random.randint(-15,15)/100)
        
def learn(trainingSize):
    
    currentPlayer= chooseAlternateStartPlayer()
    count = 0
    while(count< trainingSize):
        showBoard()
        nextMove= chooseRandomMove()
        key= currentPlayer + ''.join(boardState) + str(nextMove)
    
        if key not in Q_table:
            Q_table[key]= random.randint(-15,15)/100
        
        tempState=list(boardState)
        tempState[nextMove]=currentPlayer
        
        boolGameOver= 1
        for i in range(9):
            if tempState[i]=='-':
                boolGameOver=0
                break
        
        if not boolGameOver:
        
            key= changePlayer(currentPlayer) + ''.join(tempState) + str(nextMove)

            if key not in Q_table:
                newKey= currentPlayer + ''.join(tempState)
                
                for move in range (9):
                    Q_table[newKey+ str(move)]= random.randint(-15,15)/100
        
            updateQTable(currentPlayer, nextMove)

            
        gameResult=finalState(boardState)
        print(gameResult)
        
        if gameResult=='x' or gameResult=='d' or gameResult=='o':
            initializeBoard()
            count+=1
        else:
            
            boardState[nextMove]=currentPlayer
            currentPlayer=changePlayer(currentPlayer)
            
        

def updateQTable(player, nextMove):
    
    gameResult=finalState(boardState)
    if gameResult=='x' or gameResult=='d' or gameResult=='o':
        expected = returnReward(gameResult, boardState)
    else:
        tempState=list(boardState)
        tempState[nextMove]=player
        
        if player=='x':
            expected = float(returnReward(finalState(tempState), tempState) + (discount * minQ(player, nextMove)))
        else:
            expected = float(returnReward(finalState(tempState), tempState) + (discount * maxQ(player, nextMove)))
        
    change = learningRate * (expected - float(Q_table[player + ''.join(boardState)+ str(nextMove)]))
            
    Q_table[player + ''.join(boardState)+str(nextMove)] = str(float(Q_table[player + ''.join(boardState)+str(nextMove)]) + change)
    
    
def minQ(currentPlayer, move):
    
    tempState=list(boardState)
    tempState[move]=currentPlayer
    
    lastMove=1
    for i in range(9):
        if tempState[i]=='-':
            lastMove=0
            break
    
    if lastMove==1:
        return 0
    
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMin=10
        
        if key+str(i) in Q_table:
            
            if tempMin>float(Q_table[key + str(i)]):
                tempMin=float(Q_table[key + str(i)])
         
    return tempMin
    
def maxQ(currentPlayer, move):
    
    tempState=list(boardState)
    tempState[move]=currentPlayer
    key= changePlayer(currentPlayer) + ''.join(tempState)
    
    
    for i in range(9):
        
        tempMax=-10
        
        if key+str(i) in Q_table:
            
            if tempMax>float(Q_table[key + str(i)]):
                tempMax=float(Q_table[key + str(i)])
         
    return tempMax
           
    
def finalState(boardState):
    
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
    
    

def returnReward(gameResult, boardState):
    
    if gameResult=='x':
        return float(1.0)
    if gameResult=='o':
        return float(-1.0)
    if gameResult=='not over' or finalState(boardState)=='d':
        return float(0.0)

    
def changePlayer(player):
    if player=='o':
        return 'x'
    else:
        return 'o'
    
def showBoard():
    print('\n')
    print(boardState[0]+boardState[1]+boardState[2])
    print(boardState[3]+boardState[4]+boardState[5])
    print(boardState[6]+boardState[7]+boardState[8])
    return 


initializeBoard()
initializeQValues()

learn(100000)
print(Q_table)
    
