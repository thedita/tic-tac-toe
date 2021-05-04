# Game of Tic-Tac-Toe
# Thedita Pedersen
# 05/03/2021

# To Do: Code How to check if player has won the game

#Classes
class Player:
    has_won = False

    def __init__(self, name):
        self.name = name
        self.moves = []
    
    def make_move(self):
        move_msg = "Player {PLAYER}: Make your move from these possible moves:"
        print(move_msg.format(PLAYER=self.name))
    
        for move in possible_moves:
            print(move)

        self.move = input("What is your move?: \n")
        possible_moves.remove(self.move)
        self.moves.append(self.move)



    
# Welcome The Player
print("Tic-Tac-Toe: A Game for Warriors")
print("By Thedita Pedersen")

# Two Player or One Player?
which_game = input("1 or 2 Players?\n")

# Game Board
possible_moves = ["top right", "top middle", "top left", "middle right", "center", "middle left", "bottom right", "bottom middle", "bottom left"]
winning_moves = [[1, 4, 7], [1, 2, 3], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]]

# Two Player Game
if "2" or "two" in lower(which_game):
    player1 = Player("1")
    player2 = Player("2")

player1.make_move()
player2.make_move()

# One Player Game


