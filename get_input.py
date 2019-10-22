import sys
import rubik_representation as rubik
import moves as mv
import colors as col

def get_args():
	list_of_moves = []
	i = 0
	move = "null"
	while i < len(sys.argv[1]) - 1:
		if sys.argv[1][i] != ' ' and sys.argv[1][i + 1] == ' ':
			move = str(sys.argv[1][i])
			list_of_moves.append(move)
		elif sys.argv[1][i] != ' ' and sys.argv[1][i + 1] != ' ':
			move = str(sys.argv[1][i]) + str(sys.argv[1][i + 1])
			list_of_moves.append(move)
			i += 1
		elif sys.argv[1][i] == ' ' and i + 1 == len(sys.argv[1]):
			move = str(sys.argv[1][i + 1])
			list_of_moves.append(move)
		i += 1
	print(col.GREEN + "List of moves as input : " + col.RESET)
	print(list_of_moves)
	print("\n")
	return (list_of_moves)