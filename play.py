#start play.py
#by default, the human is the first player
#enter the index where you want to play your move

import random

import pickle


#player Tag is set to 'o' by default
playerTag='o'

boardState=[]
for i in range (9):                               
    boardState.append('-')
    
    
def initializeBoard():
    
    for i in range (9):                               
        boardState[i]='-'
    
    return
def showBoard(boardState):
    print('\n')
    print(boardState[0]+boardState[1]+boardState[2])
    print(boardState[3]+boardState[4]+boardState[5])
    print(boardState[6]+boardState[7]+boardState[8])
    return 

def PlayWithAICompStarts(humanTag):
    initializeBoard()
    if humanTag=='x':
        AiTag='o'
    else:
        AiTag='x'
        
    while finalState(boardState)=='not over':
        
        
        boardState[int(chooseNextMove(AiTag))]=AiTag
    
        if finalState(boardState)==humanTag:
            print("You win")
            break
        elif finalState(boardState)==AiTag:
            print("AI wins")
            break   
        elif finalState(boardState)=='d':
            print("Draw")
            break
        showBoard(boardState)
            
        validInput=0
        while validInput==0:
            humanNextMoveIndex= input()
            if(boardState[int(humanNextMoveIndex)]!='-'):
                print('invalid move.')
            else:
                validInput=1
                
        
            
        boardState[int(humanNextMoveIndex)]= humanTag
        
        if finalState(boardState)==humanTag:
            print("You win")
            break
        elif finalState(boardState)==AiTag:
            print("AI wins")
            break
        elif finalState(boardState)=='d':
            print("Draw")
            break
       
    return 
def PlayWithAI(humanTag):
    initializeBoard()
    if humanTag=='x':
        AiTag='o'
    else:
        AiTag='x'
        
    while finalState(boardState)=='not over':
        showBoard(boardState)
        
        validInput=0
        while validInput==0:
            humanNextMoveIndex= input()
            if(boardState[int(humanNextMoveIndex)]!='-'):
                print('invalid move.')
            else:
                validInput=1
        boardState[int(humanNextMoveIndex)]= humanTag
        
        if finalState(boardState)==humanTag:
            print("You win")
            break
        elif finalState(boardState)==AiTag:
            print("AI wins")
            break
        elif finalState(boardState)=='d':
            print("Draw")
            break
        boardState[int(chooseNextMove(AiTag))]=AiTag
    
        if finalState(boardState)==humanTag:
            print("You win")
            break
        elif finalState(boardState)==AiTag:
            print("AI wins")
            break   
        elif finalState(boardState)=='d':
            print("Draw")
            break
    return 

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
    
def chooseRandomMove():
    r=[]
    for i in range(9):
        if boardState[i]=='-':
            r.append(i)
    if len(r)>0:
        return r[random.randint(0,len(r)-1)]
    else:
        return -1
    
    
def chooseNextMove(AiTag):
    
    if AiTag=='o':
        
        key = AiTag + ''.join(boardState)
        tempMin=10000
        index=-1
        for i in range(9):

            
            if key+str(i) in Q_table:

                if tempMin>float(Q_table[key + str(i)]):
                    tempMin=float(Q_table[key + str(i)])
                    index=i
        
        if index!=-1:
            return index
        
        else:
            print("random move chosen.")
            return chooseRandomMove()
    
    if AiTag=='x':
        
        key = AiTag + ''.join(boardState)
        tempMax=-10000
        index=-1
        for i in range(9):

            
            if key+str(i) in Q_table:

                if tempMax<float(Q_table[key + str(i)]):
                    tempMax=float(Q_table[key + str(i)])
                    index=i
                    
        if index!=-1:
            return index
        
        else:
            print("random move chosen.")
            return chooseRandomMove()
        

pickle_in = open("qValues.pickle","rb")
Q_table = pickle.load(pickle_in)


#for key in sorted(Q_table):
    
#  showBoard(list(key[1:10]))
#  print("current player:", key[0])
#  print("move index", key[10])
#  print("Q_value", Q_table[key])   
    
    
#ke='x--x-oo-ox'

#print(len(Q_table))
#for i in range(9):
    #if ke+str(i) in Q_table:
        #print(str(i),Q_table[ke+str(i)])
        
print("Enter 'y' if you want to be the first player and 'n' otherwise")
temp=input()
if temp=='y':
    PlayWithAI(playerTag)
elif temp=='n':
    PlayWithAICompStarts(playerTag)