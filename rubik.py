import moves as mv
import initial_state as in_st
import scramble as sc
import test_moves as t_mv 

print("Initial State of Rubik")
t_mv.print_initial_state()

sc.get_args()
sc.rubik_scramble()
print("Front Side")
print(in_st.front_side)
print("Back Side")
print(in_st.back_side)
print("Left Side")
print(in_st.left_side)
# t_mv.testing_moves()