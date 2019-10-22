# import rubik_representation as rubik
import moves as mv
import colors as col

def phase1(rubik):
	print(col.GREEN + "Phase1 Moves" + col.RESET)
	rubik.upper_side = mv.move_u(rubik.upper_side)
	rubik.down_side = mv.move_d(rubik.down_side)
	rubik.left_side = mv.move_l(rubik.left_side)
	rubik.right_side = mv.move_r(rubik.right_side)
	rubik.front_side = mv.move_f_double(rubik.front_side)
	rubik.back_side = mv.move_b_double(rubik.back_side)
	print "\n"