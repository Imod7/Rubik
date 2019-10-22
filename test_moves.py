import initial_state as in_st
import moves as mv

# checking that moves are working correctly

def testing_moves():
	print("Testing Moves")

	print("Left Side Initial")
	print(in_st.left_side)
	in_st.left_side = mv.move_l(in_st.left_side)
	in_st.left_side = mv.move_l_prime(in_st.left_side)
	in_st.left_side = mv.move_l_double(in_st.left_side)
	print("\n")

	print("Right Side Initial")
	print(in_st.right_side)
	in_st.right_side = mv.move_r(in_st.right_side)
	in_st.right_side = mv.move_r_prime(in_st.right_side)
	in_st.right_side = mv.move_r_double(in_st.right_side)
	print("\n")

	print("Up Initial")
	print(in_st.upper_side)
	in_st.upper_side = mv.move_u(in_st.upper_side)
	in_st.upper_side = mv.move_u_prime(in_st.upper_side)
	in_st.upper_side = mv.move_u_double(in_st.upper_side)
	print("\n")

	print("Down Initial")
	print(in_st.down_side)
	in_st.down_side = mv.move_d(in_st.down_side)
	in_st.down_side = mv.move_d_prime(in_st.down_side)
	in_st.down_side = mv.move_d_double(in_st.down_side)
	print("\n")

	print("Front Side Initial")
	print(in_st.front_side)
	in_st.front_side = mv.move_f(in_st.front_side)
	in_st.front_side = mv.move_f_prime(in_st.front_side)
	in_st.front_side = mv.move_f_double(in_st.front_side)
	print("\n")

	print("Back Initial")
	print(in_st.back_side)
	in_st.back_side = mv.move_b(in_st.back_side)
	in_st.back_side = mv.move_b_prime(in_st.back_side)
	in_st.back_side = mv.move_b_double(in_st.back_side)
	print("\n")
