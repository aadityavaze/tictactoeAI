import random

import pickle

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
        showBoard(boardState)
        boardState[int(chooseNextMove(AiTag))]=AiTag
        
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
        

pickle_in = open("qValues.pickle","rb")
Q_table = pickle.load(pickle_in)
ke='xoo--x--xo'

for i in range(9):
    if ke+str(i) in Q_table:
        print(str(i),Q_table[ke+str(i)])
        
PlayWithAI('x')