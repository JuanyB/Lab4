class BoardClass:
    ''' 
    Sets the attributes for the player user names, number of wins, ties, and losses. Contains the functions that update of the number of games playes, 
    resets the board, and updates the board. Also functions to check who won, if the board is full, and that prints the stats of the game.
    '''
    #
    def __init__(self, player1: str='', player2: str='', move: int=0, mark: str='X') -> None:
        self.player1 = player1
        self.player2 = player2
        self.move = move
        self.numberOfWins = 0
        self.numberOfLosses = 0
        self.numberOfTies = 0
        self.num_games = 1
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ','-']]
        self.empty_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ','-']]
        self.boardDisplay = ''
        self.mark = mark
        

    def resetGameBoard(self) -> None:
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ','-']]
        
    def updateGamesPlayed(self) -> None:
        self.num_games += 1
    def IncrementLosses(self):
        self.numberOfLosses += 1
    def IncrementTies(self):
        self.numberOfTies += 1
    def IncrementWins(self):
        self.numberOfWins += 1
    def computeStats(self):
        stats = f"Player 1: {self.player1}\n"
        stats += f"Player 2: {self.player2}\n"
        stats += f"Number of Games: {self.num_games}\n"
        stats += f"Number of Wins: {self.numberOfWins}\n"
        stats += f"Number of Losses: {self.numberOfLosses}\n"
        stats += f"Number of Ties: {self.numberOfTies}"
        return stats

    def boardIsFull(self) -> bool:
        space_counter = 0
        for row in self.board:
            for space in row:
                if space == ' ' or space == '-':
                    return False
                elif space != ' ' or space != '-':
                    space_counter += 1
        if space_counter == 9:
            self.numberOfTies += 1
            return True
        
    
    
    #Returns boolean value of whether or not a player has won
    def isWinner(self):
        #Checking if there are three in a row horizontally
        win = False
        x_threeInARow = 0
        o_threeInARow = 0
        for row in self.board:
            if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
                return 'X Wins!'
            elif row[0] == 'O' and row[1] == 'O' and row[2] == 'O':
                return 'O Wins!'
            
                                        
        #Checking to see if there are three in a row vertically
        x_vert = 0
        o_vert = 0
        for x_row in range(3):
            for y_row in range(3):
                if self.board[y_row][x_row] == 'X':
                    x_vert += 1
                elif self.board[y_row][x_row] == 'O':
                    o_vert += 1
                    
            if x_vert == 3:
                return 'X Wins!'
            else:
                x_vert = 0
                
            if o_vert == 3:
                return 'O Wins!'
            else:
                o_vert = 0
                        
        #Checking if there are three in a row diagonally
        if (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X'):
            return 'X Wins!'
        elif (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
            return 'X Wins!'
        elif (self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O'):
            return 'O Wins!'
        elif (self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'):
            return 'O Wins!'

        return False
        

    def display_board(self):
        self.boardDisplay = ''
        for row in self.board:
            if row != self.base_board[2]:
                for square in row[0:2]:
                    self.boardDisplay += f'{square}|'
                self.boardDisplay += f'{row[2]}'
                self.boardDisplay += f'\n'
                self.boardDisplay += f'-+-+-'
                self.boardDisplay += f'\n'
            else:
                for square in row:
                    if square == '-':
                        self.boardDisplay += f'{square}'
                    else:
                        self.boardDisplay += f'{square}|'
                self.boardDisplay += f'\n'
        return self.boardDisplay

    #def player1_turn(self) -> bool:
        #if self.mark == 'X':
            #self.mark = 'O'
            #return True
            
        #else:
            #self.mark = 'X'
            #return False
    def updateGameBoard(self, move, mark):
        if move in range(1, 4):
            if (self.board[0][(move - 1)] == ' '):
                self.board[0][(move - 1)] = mark
            else:
                print("Spot is taken!")
        elif move in range(4, 7):
            if move == 4:
                if (self.board[1][0] == ' '):
                    self.board[1][0] = mark
                else:
                    print("Spot is taken!")
            if move == 5:
                if (self.board[1][1] == ' '):
                    self.board[1][1] = mark
                else:
                    print("Spot is taken!")
            if move == 6:
                if (self.board[1][2] == ' '):
                    self.board[1][2] = mark
                else:
                    print("Spot is taken!")
        elif move in range(7, 10):
            if move == 7:
                if (self.board[2][0] == ' '):
                    self.board[2][0] = mark
                else:
                    print("Spot is taken!")
            if move == 8:
                if (self.board[2][1] == ' '):
                    self.board[2][1] = mark
                else:
                    print("Spot is taken!")
            if move == 9:
                if (self.board[2][2] == '-'):
                    self.board[2][2] = mark
                else:
                    print("Spot is taken!")
            if move == 10:
                print('Invalid move, please choose a number 1-9')
        elif move >= 10:
             print('Invalid move, please choose a number 1-9')

    #def play_board(self, player='X'):
        #self.resetGameBoard()
        #run = True
        
        
        #while run:
            #self.display_board()
            #self.updateGameBoard(self.move)
            
            #if self.isWinner(player) == True:
                #print(f'{player} has won the game!')
                #run = False
                #break
            #if self.boardIsFull() == True:
                #print('Tie!')
                #run = False 
                #break




        
        
        
