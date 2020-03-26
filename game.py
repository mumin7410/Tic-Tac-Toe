board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',]

gamestillrunnig = True
currentplayer = 'x' 
winner = None

def playgame():
    display_board()
    
    while gamestillrunnig:
        Handle(currentplayer)
        checkgameover()
        fliphandleplayer()

    if winner == 'x' or winner == 'o':
        print(winner + ' won')
    if winner == None:
        print('Tie')

def display_board ():
    
    print (board[0] , '|' , board[1], '|', board[2])
    print (board[3] , '|' , board[4], '|', board[5])
    print (board[6] , '|' , board[7], '|', board[8])


def Handle (player):
    position = int(input('Choose 0-8: '))
    board[position] = player
    display_board()

def checkgameover():
    win()
    tie()
    return

def win():
    global winner
    rowwinner = checkrow()
    columnwinner = checkcolumn()
    diagwinner = checkdiag()
    
    if rowwinner:
        winner = rowwinner
    elif columnwinner:
        winner = columnwinner
    elif diagwinner:
        winner = diagwinner
    else:
        winner = None
        return
    
def checkcolumn():
    global winner
    global gamestillrunnig
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    if column_1 or column_2 or column_3:
        gamestillrunnig = False
    if column_1 :
        return board[0]
    if column_2 :
        return board[1]
    if column_3 :
        return board[2]

    return

def checkrow():
    global gamestillrunnig
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        gamestillrunnig = False
    if row_1 :
        return board[0]
    if row_2 :
        return board[3]
    if row_3 :
        return board[6]
    return

def checkdiag():
    global gamestillrunnig
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[6] == board[4] == board[2] != '-'
    if diag_1 or diag_2 :
        gamestillrunnig = False
    if diag_1 :
        return board[0]
    if diag_2 :
        return board[6]
    return



def tie ():
    global gamestillrunnig
    if '-' not in board:
        gamestillrunnig = False
    return 

def fliphandleplayer():
    global currentplayer 
    if currentplayer == 'x':
        currentplayer ='o'
    elif currentplayer == 'o':
        currentplayer = 'x'
    return 

playgame()

#test commit




















    





    



    
    

    