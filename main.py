import pygame
import sys

pygame.init()
#la dimenssion du tableau
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grille 3x3")

# couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# tableau
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# Fonction pour afficher la grille
def draw_board():
    for i in range(1, 3):
        # Lignes verticales
        pygame.draw.line(screen, black, (i * width // 3, 0), (i * width // 3, height), 2)
        # Lignes horizontales
        pygame.draw.line(screen, black, (0, i * height // 3), (width, i * height // 3), 2)

# Fonction pour afficher les symboles sur la grille
def draw_symbols():
    font = pygame.font.Font(None, 250)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                text = font.render("X", True, black)
                screen.blit(text, (j * width // 3 + 30, i * height // 3 + 30))
            elif board[i][j] == "O":
                text = font.render("O", True, black)
                screen.blit(text, (j * width // 3 + 30, i * height // 3 + 30))

# Fonction pour vérifier s'il y a une victoire
def check_winner():
    # Vérifier les lignes et les colonnes
    for i in range(3):
        if all(board[i][j] == "X" for j in range(3)) or all(board[j][i] == "X" for j in range(3)):
            return "X"
        elif all(board[i][j] == "O" for j in range(3)) or all(board[j][i] == "O" for j in range(3)):
            return "O"

    # Vérifier les diagonales
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X"
    elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O"

    return None

# Fonction principale du jeu
def main():
    turn = "X"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // (height // 3)
                col = x // (width // 3)

                if board[row][col] == "":
                    board[row][col] = turn

                    winner = check_winner()
                    if winner:
                        print(f"Le joueur {winner} a gagné !")
                        pygame.quit()
                        sys.exit()

                    turn = "O" if turn == "X" else "X"

        screen.fill(white)
        draw_board()
        draw_symbols()
        pygame.display.flip()

if __name__ == "__main__":
    main()





