import random
import pickle

#Representations used
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
# so the above state is represented as appended string player + board state
#Eg. 'ooxooxx---' represents a state mentioned above with o's turn to play

#State appended to an action(index denoting next move) is mapped to expected rewards and stored in Q_table
#Eg. 'ooxooxx---7' represents a state mentioned above with o's turn to play and a move to play at index 7



Q_table=  {}

discount=0.94
learningRate=0.2

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
    

def determineNextMoveforTraining(currentPlayer):
    
    
    temp= random.randint(0,100)
        
    #if temp > (0.9-0.8*len(Q_table)/100000)*100:

    if temp > 30:       
        return chooseNextMove(currentPlayer)
    else:
        return chooseRandomMove()
            
        

def initializeQValues():
    
    newKeyo= 'o---------'
    newKeyx= 'x---------'
    for move in range (9):
        Q_table[newKeyo+str(move)]= str(random.randint(-15,15)/100)
        Q_table[newKeyx+str(move)]= str(random.randint(-15,15)/100)
        
def learn(trainingSize):
    
    currentPlayer= chooseAlternateStartPlayer()
    count = 0
    while(count< trainingSize):
        
        showBoard(boardState)
        nextMove= determineNextMoveforTraining(currentPlayer)
        
        key= currentPlayer + ''.join(boardState) + str(nextMove)
    
        if key not in Q_table:
            Q_table[key]= random.randint(-15,15)/100
        
        tempState=list(boardState)
        tempState[nextMove]=currentPlayer
        gameRes=finalState(tempState)
        
        if gameRes=='not over':
            
            tableEntryExists=0
            
            for i in range(9):
                ke= changePlayer(currentPlayer) + ''.join(tempState) + str(i)
                
                if ke in Q_table:
                    tableEntryExists=1
                    break
            
            
            if tableEntryExists==0:
                newKey= changePlayer(currentPlayer) + ''.join(tempState)
                r=[]
                for i in range(9):
                    if tempState[i]=='-':
                        r.append(i)
                        
                for move in range (len(r)):
                    Q_table[newKey+ str(r[move])]= random.randint(-15,15)/100
        
            updateQTable(currentPlayer, nextMove)

            
        gameResult=finalState(tempState)
        print(gameResult)
        
        if gameResult=='x' or gameResult=='d' or gameResult=='o':
            initializeBoard()
            count+=1
        else:
            boardState[nextMove]=currentPlayer
            currentPlayer=changePlayer(currentPlayer)
            
        

def updateQTable(player, nextMove):
    
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
        
        tempMin=10000
        
        if key+str(i) in Q_table:
            
            if tempMin>float(Q_table[key + str(i)]):
                tempMin=float(Q_table[key + str(i)])
         
    return tempMin
    
def maxQ(currentPlayer, move):
    
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
        
        tempMax=-10000
        
        if key+str(i) in Q_table:
            
            if tempMax<float(Q_table[key + str(i)]):
                tempMax=float(Q_table[key + str(i)])
         
    return tempMax
    
def finalState(boardState):
    
    if (boardState[0]==boardState[1]==boardState[2]=='x') or (boardState[0]==boardState[1]==boardState[2]=='o'):
        return boardState[0]
        
    if (boardState[3]==boardState[4]==boardState[5]=='x') or (boardState[3]==boardState[4]==boardState[5]=='o'):
        return boardState[3]
    
    if (boardState[6]==boardState[7]==boardState[8]=='x') or (boardState[6]==boardState[7]==boardState[8]=='o'):
        return boardState[6]
    
    if (boardState[0]==boardState[3]==boardState[6]=='x') or (boardState[0]==boardState[3]==boardState[6]=='o'):
        return boardState[0]
        
    if (boardState[1]==boardState[4]==boardState[7]=='x') or (boardState[1]==boardState[4]==boardState[7]=='o'):
        return boardState[1]
    
    if (boardState[2]==boardState[5]==boardState[8]=='x') or (boardState[2]==boardState[5]==boardState[8]=='o'):
        return boardState[2]
    
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
    
def showBoard(boardState):
    print('\n')
    print(boardState[0]+boardState[1]+boardState[2])
    print(boardState[3]+boardState[4]+boardState[5])
    print(boardState[6]+boardState[7]+boardState[8])
    return 

def PlayWithAI(humanTag):
    initializeBoard()
    if humanTag=='x':
        AiTag='o'
    else:
        AiTag='x'
        
    while finalState(boardState)=='not over':
        showBoard(boardState)
        humanNextMoveIndex= input()
        boardState[int(humanNextMoveIndex)]= humanTag
        boardState[int(chooseNextMove(AiTag))]=AiTag
            
def chooseNextMove(AiTag):
    
    if AiTag=='o':
        
        key = AiTag + ''.join(boardState)
        
        for i in range(9):

            tempMin=10000
            index=-1
            if key+str(i) in Q_table:

                if tempMin>float(Q_table[key + str(i)]):
                    index=i
        
        if index!=-1:
            return index
        
        else:
            print("random move chosen.")
            return chooseRandomMove()
    
    if AiTag=='x':
        
        key = AiTag + ''.join(boardState)
        
        for i in range(9):

            tempMax=-10000
            index=-1
            if key+str(i) in Q_table:

                if tempMax<float(Q_table[key + str(i)]):
                    index=i
                    
        if index!=-1:
            return index
        
        else:
            return chooseRandomMove()
        

initializeBoard()
initializeQValues()

learn(50000)

pickle_out = open("qValues.pickle","wb")
pickle.dump(Q_table, pickle_out)
pickle_out.close()

#for key in Q_table:
    #showBoard(list(key[1:10]))
    #print("current player:", key[0])
    #print("move index", key[10])
    #print("Q_value", Q_table[key])   
    

