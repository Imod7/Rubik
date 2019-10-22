import rubik_representation as rubik
import moves as mv

# checking that moves are working correctly

def testing_moves():
	print("Testing Moves")

	print("Left Side Initial")
	print(rubik.left_side)
	rubik.left_side = mv.move_l(rubik.left_side)
	rubik.left_side = mv.move_l_prime(rubik.left_side)
	rubik.left_side = mv.move_l_double(rubik.left_side)
	print("\n")

	print("Right Side Initial")
	print(rubik.right_side)
	rubik.right_side = mv.move_r(rubik.right_side)
	rubik.right_side = mv.move_r_prime(rubik.right_side)
	rubik.right_side = mv.move_r_double(rubik.right_side)
	print("\n")

	print("Up Initial")
	print(rubik.upper_side)
	rubik.upper_side = mv.move_u(rubik.upper_side)
	rubik.upper_side = mv.move_u_prime(rubik.upper_side)
	rubik.upper_side = mv.move_u_double(rubik.upper_side)
	print("\n")

	print("Down Initial")
	print(rubik.down_side)
	rubik.down_side = mv.move_d(rubik.down_side)
	rubik.down_side = mv.move_d_prime(rubik.down_side)
	rubik.down_side = mv.move_d_double(rubik.down_side)
	print("\n")

	print("Front Side Initial")
	print(rubik.front_side)
	rubik.front_side = mv.move_f(rubik.front_side)
	rubik.front_side = mv.move_f_prime(rubik.front_side)
	rubik.front_side = mv.move_f_double(rubik.front_side)
	print("\n")

	print("Back Initial")
	print(rubik.back_side)
	rubik.back_side = mv.move_b(rubik.back_side)
	rubik.back_side = mv.move_b_prime(rubik.back_side)
	rubik.back_side = mv.move_b_double(rubik.back_side)
	print("\n")
