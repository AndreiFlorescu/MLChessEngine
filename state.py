import chess

class State():
	def __init__(self):
		self.board = chess.Board()

	def serialize(self):
		pass

	def possible_moves(self):
		return self.board.legal_moves


if __name__ == "__main__":
	s = State()
	print(s.board)
