import rubik_representation as rubik
import moves as mv
import colors as col

def rubik_scramble(moves):
	print(col.GREEN + "Scrambling the Rubik's Cude based on the input" + col.RESET)
	for list_item in moves:
		if list_item == "L":
			rubik.left_side = mv.move_l(rubik.left_side)
		elif list_item == "L'":
			rubik.left_side = mv.move_l_prime(rubik.left_side)
		elif list_item == "L2":
			rubik.left_side = mv.move_l_double(rubik.left_side)
		elif list_item == "R":
			rubik.right_side = mv.move_r(rubik.right_side)
		elif list_item == "R'":
			rubik.right_side = mv.move_r_prime(rubik.right_side)
		elif list_item == "R2":
			rubik.right_side = mv.move_r_double(rubik.right_side)
		elif list_item == "U":
			rubik.upper_side = mv.move_u(rubik.upper_side)
		elif list_item == "U'":
			rubik.upper_side = mv.move_u_prime(rubik.upper_side)
		elif list_item == "U2":
			rubik.upper_side = mv.move_u_double(rubik.upper_side)
		elif list_item == "D":
			rubik.down_side = mv.move_d(rubik.down_side)
		elif list_item == "D'":
			rubik.down_side = mv.move_d_prime(rubik.down_side)
		elif list_item == "D2":
			rubik.down_side = mv.move_d_double(rubik.down_side)
		elif list_item == "F":
			rubik.front_side = mv.move_f(rubik.front_side)
		elif list_item == "F'":
			rubik.front_side = mv.move_f_prime(rubik.front_side)
		elif list_item == "F2":
			rubik.front_side = mv.move_f_double(rubik.front_side)
		elif list_item == "B":
			rubik.back_side = mv.move_b(rubik.back_side)
		elif list_item == "B'":
			rubik.back_side = mv.move_b_prime(rubik.back_side)
		elif list_item == "B2":
			rubik.back_side = mv.move_b_double(rubik.back_side)
	print "\n"