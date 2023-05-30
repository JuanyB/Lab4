import tkinter as tk
class BoardClass:
    ''' 
    Sets the attributes for the player user names, number of wins, ties, and losses. Contains the functions that update of the number of games playes, 
    resets the board, and updates the board. Also functions to check who won, if the board is full, and that prints the stats of the game.
    '''
    master = None
    def __init__(self, player1: str='', player2: str='', move: int=0) -> None:
        self.starter_things(player1, player2, move)
        
        self.canvasSetup()
        self.runUI()
        
    
        

    def resetGameBoard(self) -> None:
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ', ' ']]
        
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
        
    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("Tic Tac Toe")
        self.master.configure(background='lightblue')
    def restart
    def runUI(self):
        self.master.mainloop()


    def boardIsFull(self) -> bool:
        for row in self.board:
            for space in row:
                if space == ' ':
                    return False
                elif space == '-':
                    return False
                else:
                    return True
    
    
    #Returns boolean value of whether or not a player has won
    def isWinner(self, mark) -> bool:
        #Checking if there are three in a row horizontally
        threeInARow = 0
        for x_row in range(3):
            for y_row in range(3):
                if self.board[x_row][y_row] == mark:
                    threeInARow += 1

        if threeInARow == 3:
            return True
        
        #Checking to see if there are three in a row vertically
        threeVert = 0
        for x_row in range(3):
            for y_row in range(3):
                if self.board[y_row][x_row] == mark:
                    threeVert += 1
        if threeVert == 3:
            return True
        #Checking if there are three in a row diagonally
        if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark: return True

        if self.board[0][2] == mark and self.board[1][1] == mark and self.board[2][0] == mark: return True

        return False

    def display_board(self):
        
        for row in self.board:
            if row != self.board[2]:
                self.boardDisplay += f'{row[0]}|row[1]|row[2]'
                self.boardDisplay += f'\n'
                self.boardDisplay += f'-+-+-+-'
                self.boardDisplay += f'\n'
            else:
                self.boardDisplay += f'{row[0]}|{row[1]}|{row[2]}'
                self.boardDisplay += f'\n'
        return self.boardDisplay

    
    def updateGameBoard(self, move):
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
                    if (self.board[2][2] == ' '):
                        self.board[2][2] = mark
                    else:
                        print("Spot is taken!")
                if move == 10:
                    print('Invalid move, please choose a number 1-9')
            elif move >= 10:
                 print('Invalid move, please choose a number 1-9')
    def starter_things(self, player1: str='', player2: str='', move: int=0):
        self.player1 = player1
        self.player2 = player2
        self.move = move
        self.numberOfWins = 0
        self.numberOfLosses = 0
        self.numberOfTies = 0
        self.num_games = 1
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ', ' ']]
        self.empty_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ', ' ']]
        
if __name__ == '__main__':
    gameboard = BoardClass()
