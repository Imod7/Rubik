import rubik_representation as rubik
import colors as col

# printing initial state of Rubik

def print_rubik_sides():
	print(col.YELLOW + "FrontSide Initial" + col.RESET)
	print(rubik.front_side)
	print(col.YELLOW + "BackSide Initial" + col.RESET)
	print(rubik.back_side)
	print(col.YELLOW + "UpperSide Initial" + col.RESET)
	print(rubik.upper_side)
	print(col.YELLOW + "DownSide Initial" + col.RESET)
	print(rubik.down_side)
	print(col.YELLOW + "LeftSide Initial" + col.RESET)
	print(rubik.left_side)
	print(col.YELLOW + "RightSide Initial" + col.RESET)
	print(rubik.right_side)
	print("\n")

