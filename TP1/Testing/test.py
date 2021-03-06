from Heuristics.minimumMatchingLowerBound import mmlb
from goal import Goal
from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs
from NonInformative.dfs import dfs
from NonInformative.iddfs import iddfs

from solution import Solution
import json

with open('testConfig.json') as config_file:
    data = json.load(config_file)
    config_file.close()

algorithm = data['algorithm']
game_map = data['map']
print("Chosen algorithm is:", algorithm)
print("Board:")
print()

with open(game_map) as game_map_file:
    lines = game_map_file.readlines()

height = len(lines)
width = len(lines[0])-1

board = [['0' for i in range(width)] for j in range(height)]
boxes = []
goals = []
player = Player(0, 0)

for x, line in enumerate(lines):
    for y, char in enumerate(line[:-1]):
        if char == 'P':
            player = Player(x, y)
            board[x][y] = '.'
        elif char == '#':
            boxes.append(Box(x, y))
            board[x][y] = '.'
        elif char == '+':
            goals.append(Goal(x, y))
            board[x][y] = char
        else:
            board[x][y] = char

for box in boxes:
    print(box)

board = Board(board, height, width, goals)
#board.print_state(player=player, boxes=boxes)

node = Node(player, boxes)
game = GameController(board)

mmlb(board, boxes)
"""
if algorithm == "bfs":
    game_solution = bfs(game, node)
    if game_solution.solved:
        game.print_path(game_solution.path)
        print("Processing time: ", game_solution.processing_time)
        print("Deepness: ", game_solution.expanded)
    else:
        print("Solution not found.")
elif algorithm == "dfs":
    game_solution = dfs(game, node)
    if game_solution.solved:
        game.print_path(game_solution.path)
        print("Processing time: ", game_solution.processing_time)
    else:
        print("Solution not found.")
elif algorithm == "iddfs":
    hardcoded_limit = 1000
    game_solution = iddfs(game, node, hardcoded_limit)
    if game_solution.solved:
        game.print_path(game_solution.path)
        print("Processing time: ", game_solution.processing_time)
    else:
        print("Solution not found.")

"""
