# MLChessEngine

Create a ml engine for chess.
	- use minimax
	- ml with tf for state evaluation

TO DO:
	1. 	figure out how to parse state to network
	2. 	find png archive online
	2'.	convert rawdata to usable data
	3. 	read dataset from archive

Work:

1. 	figure out how to parse state to network

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


2. 	find png archive online

Found pgn adatabase with 2.5 milion GM games:
http://www.chessgameslinks.lars-balzer.info/#large-databases_worldwide
http://rebel13.nl/rebel13/rebel%2013.html

Copied a few games in another file for testing


2'.	convert rawdata to usable data

Discoverd a problem with the pgn file. If there are empty lines inside a pgn 
game, python-chess considers what follows to belong to another pgn game.

Solution: 	Copy the file in oanothe one and remove all unecessary empty lines, 
			task done inside 'process_file.py'


3. 	read dataset from archive

Read each game from the pgn file and convert board state to a 320 bits format 
