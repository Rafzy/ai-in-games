import random
import copy
from pprint import pprint
from collections import deque
from test import PlayerAI


# class Player1AI:
#     def __init__(self):
#         self.move_num = 0
#         self.var_depth = 2
#
#     def get_move(self, game):
#         legal_moves = game.get_legal_moves()
#         # you can retrieve information from the game object
#         print("remaining walls", game.walls)
#         # print("player_positions", game.player_positions)
#         # print("board", game.board)
#         # print("P1", legal_moves)
#         # return ("U",)
#
#         # self.move_num += 1
#         # if self.move_num % 10 == 0 and self.var_depth <= 4:
#         #     self.var_depth += 1
#         # print("Curr move: ", self.move_num)
#         # print("Walls remaining", game.walls)
#
#         p1_wall = game.walls["P1"]
#         p2_wall = game.walls["P2"]
#         print("Player 1 legal moves:", legal_moves)
#         # print("Current Depth: ", self.var_depth)
#         score, best_move = self.minimax(game, depth=self.var_depth)
#         return best_move
#
#     def minimax(
#         self,
#         game,
#         depth=3,
#         maximizing_player=True,
#         alpha=float("-inf"),
#         beta=float("inf"),
#     ):
#         # Reach depth
#         if depth == 0 or self.is_game_over(game):
#             score = self.evaluate_score(game)
#             return (score, None)
#
#         legal_moves = game.get_legal_moves()
#         if not legal_moves:
#             print("Legal moves not found")
#             return (float("-inf"), None) if maximizing_player else (float("inf"), None)
#
#         best_move = None
#
#         if maximizing_player:
#             max_score = float("-inf")
#
#             for move in legal_moves:
#                 game_simulation = self.sim_move(game, move)
#                 score, _ = self.minimax(game_simulation, depth - 1, False)
#
#                 if score > max_score:
#                     max_score = score
#                     best_move = move
#
#                 alpha = max(alpha, score)
#                 if beta <= alpha:
#                     break
#
#             return (max_score, best_move)
#
#         else:
#             min_score = float("inf")
#
#             for move in legal_moves:
#                 game_simulation = self.sim_move(game, move)
#                 score, _ = self.minimax(game_simulation, depth - 1, True)
#
#                 if score < min_score:
#                     min_score = score
#                     best_move = move
#
#                 beta = min(beta, score)
#                 if beta <= alpha:
#                     break
#
#             return (min_score, best_move)
#
#     def sim_move(self, game, move):
#         game_copy = copy.deepcopy(game)
#
#         if move[0] in ["U", "L", "D", "R"]:
#             self.move(game_copy, move)
#         else:
#             self.apply_wall(game_copy, move)
#
#         return game_copy
#
#     def move(self, game, move):
#         current_player = game.players[game.ply]
#         current_position = game.player_positions[current_player]
#
#         if move[0] == "U":
#             game.player_positions[current_player] = (
#                 current_position[0] - 1,
#                 current_position[1],
#             )
#         elif move[0] == "D":
#             game.player_positions[current_player] = (
#                 current_position[0] + 1,
#                 current_position[1],
#             )
#         elif move[0] == "L":
#             game.player_positions[current_player] = (
#                 current_position[0],
#                 current_position[1] - 1,
#             )
#         elif move[0] == "R":
#             game.player_positions[current_player] = (
#                 current_position[0],
#                 current_position[1] + 1,
#             )
#
#         game.ply = (game.ply + 1) % 2
#
#     def apply_wall(self, game, move):
#         current_player = game.players[game.ply]
#         game.update_board_wall(move)
#         game.walls[current_player] -= 1
#         game.ply = (game.ply + 1) % 2
#
#     def get_valid_neighbors(self, game, position):
#         neighbors = []
#         row, col = position
#         board_size = game.board_size
#         board = game.board
#
#         if (
#             row > 0
#             and board[row - 1][col] != "H"
#             and board[row - 1][col] != "HH"
#             and board[row - 1][col] != "HV"
#         ):
#             neighbors.append((row - 1, col))
#
#         if (
#             row < board_size - 1
#             and board[row][col] != "H"
#             and board[row][col] != "HH"
#             and board[row][col] != "HV"
#         ):
#             neighbors.append((row + 1, col))
#
#         if (
#             col > 0
#             and board[row][col - 1] != "V"
#             and board[row][col - 1] != "VV"
#             and board[row][col - 1] != "HV"
#         ):
#             neighbors.append((row, col - 1))
#
#         if (
#             col < board_size - 1
#             and board[row][col] != "V"
#             and board[row][col] != "VV"
#             and board[row][col] != "HV"
#         ):
#             neighbors.append((row, col + 1))
#
#         return neighbors
#
#     def evaluate_score(self, game):
#         p1_pos = game.player_positions["P1"]
#         p2_pos = game.player_positions["P2"]
#
#         if p1_pos[0] == 0:
#             return 999
#         elif p2_pos[0] == game.board_size - 1:
#             return -999
#
#         p1_distance = self.bfs(game, p1_pos, "P1")
#         p2_distance = self.bfs(game, p2_pos, "P2")
#
#         if p1_distance == float("inf"):
#             return -999
#         elif p2_distance == float("inf"):
#             return 999
#
#         distance_score = p2_distance - p1_distance
#
#         wall_score = game.walls["P2"] - game.walls["P1"]
#
#         return distance_score + (wall_score * 0.5)
#
#     def is_game_over(self, game):
#         p1_pos = game.player_positions["P1"]
#         p2_pos = game.player_positions["P2"]
#         return p1_pos[0] == 0 or p2_pos[0] == game.board_size - 1
#
#     def bfs(self, game, s_pos, player):
#         queue = deque([(s_pos, 0)])
#         visited = set([s_pos])
#
#         goal = 0 if player == "P1" else game.board_size - 1
#
#         while queue:
#             (row, col), distance = queue.popleft()
#
#             if row == goal:
#                 return distance
#
#             for next_pos in self.get_valid_neighbors(game, (row, col)):
#                 if next_pos not in visited:
#                     visited.add(next_pos)
#                     queue.append((next_pos, distance + 1))
#
#         return float("inf")
#
#     def get_legal_directions_from_pos(self, game, from_position):
#         moves = []
#         current_position = from_position
#         board_size = game.board_size
#         board = game.board
#
#         if (
#             current_position[0] > 0
#             and board[current_position[0] - 1][current_position[1]] != "H"
#             and board[current_position[0] - 1][current_position[1]] != "HH"
#             and board[current_position[0] - 1][current_position[1]] != "HV"
#         ):
#             moves.append(("U",))
#
#         if (
#             current_position[0] < board_size - 1
#             and board[current_position[0]][current_position[1]] != "H"
#             and board[current_position[0]][current_position[1]] != "HH"
#             and board[current_position[0]][current_position[1]] != "HV"
#         ):
#             moves.append(("D",))
#
#         if (
#             current_position[1] > 0
#             and board[current_position[0]][current_position[1] - 1] != "V"
#             and board[current_position[0]][current_position[1] - 1] != "VV"
#             and board[current_position[0]][current_position[1] - 1] != "HV"
#         ):
#             moves.append(("L",))
#
#         if (
#             current_position[1] < board_size - 1
#             and board[current_position[0]][current_position[1]] != "V"
#             and board[current_position[0]][current_position[1]] != "VV"
#             and board[current_position[0]][current_position[1]] != "HV"
#         ):
#             moves.append(("R",))
#
#         return moves


class Player1AI(PlayerAI):
    def __init__(self):
        super().__init__("P1", send_it=True)
