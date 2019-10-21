import initial_state as in_st

# printing initial state of Rubik

def print_initial_state():
	print("Front Side Initial")
	print(in_st.front_side)
	print("Back Initial")
	print(in_st.back_side)
	print("Up Initial")
	print(in_st.upper_side)
	print("Bottom Initial")
	print(in_st.down_side)
	print("Left Side Initial")
	print(in_st.left_side)
	print("\n")

# checking that moves are working correctly

def testing_moves():
	print("Left Side Initial")
	print(in_st.left_side)
	print("Move L")
	in_st.left_side = mv.move_l(in_st.left_side)
	print(in_st.left_side)
	print("Move L Prime")
	in_st.left_side = mv.move_l_prime(in_st.left_side)
	print(in_st.left_side)
	print("\n")

	print("Up Initial")
	print(in_st.upper_side)
	print("Move U")
	in_st.upper_side = mv.move_u(in_st.upper_side)
	print(in_st.upper_side)
	print("Move U Prime")
	in_st.upper_side = mv.move_u_prime(in_st.upper_side)
	print(in_st.upper_side)
	print("\n")

	print("Bottom Initial")
	print(in_st.down_side)
	print("Move D")
	in_st.down_side = mv.move_d(in_st.down_side)
	print(in_st.down_side)
	print("Move D Prime")
	in_st.down_side = mv.move_d_prime(in_st.down_side)
	print(in_st.down_side)
	print("\n")

	print("Front Side Initial")
	print(in_st.front_side)
	print("Move F")
	in_st.front_side = mv.move_f(in_st.front_side)
	print(in_st.front_side)
	print("Move F Prime")
	in_st.front_side = mv.move_f_prime(in_st.front_side)
	print(in_st.front_side)
	print("\n")

	print("Back Initial")
	print(in_st.back_side)
	print("Move B")
	in_st.back_side = mv.move_b(in_st.back_side)
	print(in_st.back_side)
	print("Move B Prime")
	in_st.back_side = mv.move_b_prime(in_st.back_side)
	print(in_st.back_side)
	print("\n")
