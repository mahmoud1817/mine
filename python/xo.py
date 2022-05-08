board = [ ' ' for m in range(10) ]

def insertletter(letter,pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ' '