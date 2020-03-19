import os
import chess.pgn
from state import State


result_value = {
	'1-0': 		1,
	'0-1':		-1,
	'1/2-1/2': 	0
}

pgn = open(os.path.join('PGNDatabase', 'data.pgn'))

while 1:
	game = chess.pgn.read_game(pgn)
	
	if game == None:
		break

	result = result_value[game.headers['Result']]
	
	board = game.board()

	for move in game.mainline_moves():
		board.push(move)
		print(board)
		print()

	break
