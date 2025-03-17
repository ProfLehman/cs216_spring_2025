
# TicTacToe.py
# spring 2021
# prof. lehman
# demonstrates use of class for Tic Tac Toe game
# class includes use of docstrings to help with documentation

class TicTacToe:
    """
    class to support and play game of Tic Tac Toe
    
    uses rows 0, 1, 2 and columns 0, 1, 2 to place values

    0,0   | 0,1  | 0,2
    ------+------+-----
    1,0   | 1,1  | 1,2
    ------+------+-----
    2,0   | 2,1  | 2,2
    """
 
    def __init__(self, new_x, new_o):
        """ constructor requires player names """
        self.xPlayer = new_x
        self.oPlayer = new_o
        
        # internal data
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        self.turn = 1 # X's turn
        self.winner = "game in play"
        self.playCount = 0
        
    def __str__(self):
        """ return ASCII version of game board """
        
        result = ""
        
        for row in range(0,3):
            for col in range(0,3):
                
                # add space, X, or O
                if self.board[row][col] == 0:
                    result = result + "   "
                elif self.board[row][col] == 1:
                    result = result + " X "
                else:
                    result = result + " O "
                
                #add line spacer |
                if col == 0 or col == 1:
                    result = result + "|"
              #end for col
             
            result = result + "\n"
            
            if row == 0 or row == 1:
                result = result + "---+---+---\n"
            
            #end for row
            
        return result
        
    def isWin(self):
        """ return True if X or O win """
        win = False
        
        #list of rows and columns to check for win
        #       row0  row1  row2  col0  col1  col2  diag  diag
        rows = [0,0,0,1,1,1,2,2,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2]
        cols = [0,1,2,0,1,2,0,1,2,0,0,0,1,1,1,2,2,2,0,1,2,2,1,0]
        
        #check three rows, three columns, two diagonals
        i = 0
        while i < len(rows):
            if self.board[rows[i]][cols[i]] == self.board[rows[i+1]][cols[i+1]]:
                if self.board[rows[i+1]][cols[i+1]] == self.board[rows[i+2]][cols[i+2]]:
                    if self.board[rows[i]][cols[i]] != 0:
                        win = True
            i = i + 3
                
        return win
    
    def over(self):
        """ returns True if game is over ie. if win or 9 plays """
        gameOver = False
        
        #check for win
        if self.isWin() == True:
            gameOver = True
            if self.turn == 1:
                self.winner = self.xPlayer
            else:
                self.winner = self.oPlayer
        else:
            #check for tie
            if self.playCount == 9:
                gameOver = True
                self.winner = "Tie"

        return gameOver
    
    def play(self, r, c):
        """
        place X or O if valid reference

        parameters:
        r (int) row position 0, 1, or 2
        c (int) column position 0, 1, or 2        
        """
        #*** stub method - fix later
        #print( "you played", r, c )
        
        if r < 0 or r > 2 or c < 0 or c > 2:
            print("Error: row and col must be 0 to 2")
        else:
            if self.board[r][c] == 0:
                
                #placing 1 or 2 effectively X or O
                self.board[r][c] = self.turn
            
                self.playCount = self.playCount + 1
            
                if self.over() != True:
                    # next turn
                    if self.turn == 1:
                        self.turn = 2
                    else:
                        self.turn = 1
            else:
                print("sorry, spot taken ...")
                
    def getTurn(self):
        """ returns name of player for current turn """
        if self.turn == 1:
            return self.xPlayer
        else:
            return self.oPlayer
      
      
    def getWinner(self):
        """ returns game in play, name of winner, or tie """
        return self.winner
    
    #end class Tic Tac Toe
    
# **************************************************
# *** main *****************************************
# **************************************************

if __name__ == "__main__":
    
    #print( help(TicTacToe) ) #display class documentation
    
    game = TicTacToe("Alice", "Bernard")

    while game.over() == False:
        print( game )
        
        print( "It is {}'s turn ...".format( game.getTurn() ) )
               
        row = int(input("Enter Row: "))
        col = int(input("Enter Col: "))
        game.play(row, col)

    #show who won
    print()
    print( "{} Wins!!! ...Game Over".format( game.getWinner() ) )
    print( game )
    
    #*** end main ***
