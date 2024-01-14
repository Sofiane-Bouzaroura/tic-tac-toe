
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=8, height=4,
                                               command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} gagnant!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "C'est un match nul!")
                self.reset_board()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Check diagonal
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()





