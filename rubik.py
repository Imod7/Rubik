import moves as mv
import rubik_representation as rubik
import scramble as sc
import test_moves as t_mv 
import get_input as g_in
import printing as pr 
import colors as col
import solve_rubik as solve

list_of_moves = []
print("\n")
print(col.GREEN + "Initial State of Rubik" + col.RESET)
pr.print_rubik_sides()
list_of_moves = g_in.get_args()
sc.rubik_scramble(list_of_moves)
print(col.GREEN + "Scrambled Rubik" + col.RESET)
pr.print_rubik_sides()
print(col.GREEN + "Solving Rubik" + col.RESET)
solve.phase1(rubik)
print(col.GREEN + "Rubik State in Phase1" + col.RESET)
pr.print_rubik_sides()
# t_mv.testing_moves()