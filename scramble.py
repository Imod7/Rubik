import sys
import moves as mv
import initial_state as in_st

list_of_moves = []

def get_args():
	global list_of_moves
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
	print("List of moves : ")
	print(list_of_moves)

def rubik_scramble():
	for list_item in list_of_moves:
		if list_item == 'F':
			in_st.front_side = mv.move_f(in_st.front_side)
		elif list_item == "B":
			in_st.back_side = mv.move_b(in_st.back_side)
		elif list_item == "L":
			in_st.left_side = mv.move_l(in_st.left_side)