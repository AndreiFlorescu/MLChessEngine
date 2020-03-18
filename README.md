# MLChessEngine

Create a ml engine for chess.
	- use minimax
	- ml with tf for state evaluation

TO DO:
	1. figure out how to parse state to network
	2. find png archive online
	3. reate dataset from archive

Work:

1. figure out how to parse state to network

Possible states on board: 1 * 2 + 2 * 5 + 2 * 2 = 16 --> 4 bits

* empty / en passant move possible
* pawn w/b
* knight w/b
* bishop w/b
* rook w/b and queen/king side castle
* king w/b	
* queen w/b

state for network = 64 * 4 = 256 bits

!! NEED TO GIVE PLAYER TO MOVE !!

256 + 1 = 257 bits :/

We add another bit for each piece representation showing who will play
state for network = 64 * (4 + 1) = 320 bits