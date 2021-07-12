"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None
roundn = 1

def initial_state():
    """
    Empty 3x3 board state
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def minimax(board):
    """
    Returns best possible action for current state of the board.
    It suppose to give value 1 for winning condition for one side
    and recursivelly track it.
    
    Maximising player should pick action that produces highest max value
    Minimising player should pick action that producec lowest min value
    
    """
    if terminal(board):
        return None 
    if player(board) == X:
        val, move = fmax(board)
        return move
    else:
        val, move = fmax(board)
        return move
    

def fmin(board):
    '''
    Both min and max programmed using standard pseudocode from wikipedia page
    '''
    if terminal(board):
        return utility(board) , None
    val = -math.inf
    move = None
    for action in actions(board):
        valm, movem = fmax(result(board, action))
        if valm > val:
            val = valm
            move = action
            if val == 1:
                return val,move 
    return val, move
        


def fmax(board):
    if terminal(board):
        return utility(board) , None
    val = math.inf
    move = None
    for action in actions(board):
        valm, movem = fmin(result(board, action))
        if valm < val:
            val = valm
            move = action
            if val == -1:
                return val,move 
    return val, move
    
    
def player(board):
    """
    Returns player who has the next turn (X or O) given board
    """
    # global roundn
    # if roundn % 2 ==0:
    #     roundn+=1
    #     return O
    # else:
    #     roundn+=1
    #     return X
    xcount = 0
    ycount = 0
    for row in board:
        xcount += row.count(X)
        ycount += row.count(O)
    if xcount > ycount:
        return O
    else:
        return X 
    


def actions(board):
    """
    Returns set of all legal moves (i, j) available given the board.
    """
    actns = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actns.add((i,j))
    return actns
                
                
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the 
    copy of the board and returns the new board.
    """
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            if board[i][0] == O:
                return O
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            if board[0][j] == O:
                return O
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        if board[0][0] == O:
            return O
        
        
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        if board[0][2] == O:
            return O
    
    return None


def terminal(board):
    """
    Bool
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count+=1
    if count == 0:
        return True
    return False


def utility(board):
    """
    Utility for the algorithm.
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
       return 1
    elif winner(board) == O:
       return -1
    else:
       return 0


    
    
    
    
    
    
    
    
