import copy
from collections import deque
import random
from test import PlayerAI

#
#
# class Player2AI:
#     def __init__(self):
#         self.human_player = True  # Set to True for keyboard input, False for AI
#
#     def get_move(self, game):
#         legal_moves = game.get_legal_moves()
#         print("P2 Legal moves:", legal_moves)
#
#         if self.human_player:
#             return self.get_human_input(game, legal_moves)
#         else:
#             # AI fallback - just move down
#             return ("D",)
#
#     def get_human_input(self, game, legal_moves):
#         """Get keyboard input from human player"""
#         while True:
#             print("\nPlayer 2's turn!")
#             print("Use keys: W(up) S(down) A(left) D(right)")
#             print("For walls: type 'H row col' or 'V row col' (e.g., 'H 1 2')")
#             print("Legal moves:", legal_moves)
#
#             try:
#                 user_input = input("Player 2> ").strip().upper()
#
#                 # Handle movement keys
#                 if user_input == "W":
#                     move = ("U",)
#                 elif user_input == "S":
#                     move = ("D",)
#                 elif user_input == "A":
#                     move = ("L",)
#                 elif user_input == "D":
#                     move = ("R",)
#                 # Handle wall placement
#                 elif user_input.startswith("H ") or user_input.startswith("V "):
#                     parts = user_input.split()
#                     if len(parts) == 3:
#                         wall_type = parts[0]
#                         row = int(parts[1])
#                         col = int(parts[2])
#                         move = (wall_type, row, col)
#                     else:
#                         print("Invalid wall format! Use 'H row col' or 'V row col'")
#                         continue
#                 # Handle direct move input (fallback)
#                 else:
#                     # Try to parse as direct move like "U" or "H,1,2"
#                     if "," in user_input:
#                         parts = user_input.split(",")
#                         if len(parts) == 3:
#                             move = (parts[0], int(parts[1]), int(parts[2]))
#                         else:
#                             print("Invalid input format!")
#                             continue
#                     elif len(user_input) == 1 and user_input in "UDLR":
#                         move = (user_input,)
#                     else:
#                         print(
#                             "Invalid input! Use W/A/S/D for movement or 'H row col'/'V row col' for walls"
#                         )
#                         continue
#
#                 # Validate move
#                 if move in legal_moves:
#                     return move
#                 else:
#                     print(f"Illegal move: {move}")
#                     print(f"Legal moves are: {legal_moves}")
#                     continue
#
#             except (ValueError, IndexError):
#                 print("Invalid input format! Try again.")
#                 continue
#             except KeyboardInterrupt:
#                 print("\nGame interrupted!")
# return ("D",)  # Fallback move


class Player2AI(PlayerAI):
    def __init__(self):
        super().__init__("P2", send_it=False, soft_ff=True)
