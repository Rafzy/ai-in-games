import random


class Player1AI:
    def get_move(self, game):
        legal_moves = game.get_legal_moves()
        # you can retrieve information from the game object
        # print("remaining walls", game.walls)
        # print("player_positions", game.player_positions)
        print("board", game.board)
        # print("P1", legal_moves)
        return ("U",)
