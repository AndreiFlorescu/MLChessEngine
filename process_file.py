import os

raw_file_name = 'rawdata.pgn'

if __name__ == "__main__":
	pgn = open(os.path.join('PGNDatabase', raw_file_name))
	fileout = open(os.path.join('PGNDatabase', 'data.pgn'), 'w')

	for line in pgn:
		fileout.write(line)
		line = pgn.readline()


