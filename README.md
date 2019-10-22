# Rubik
Experimenting on how to implement the python code that solves a Rubik's cube

### How to Run
- Clone the repo
- Enter in the folder that you cloned
- Run in terminal with the following command : python rubik.py "L L' L2 R R' R2"
- The argument given in the command line can take any combination of the following letters :
  - L, L', L2, R, R', R2, U, U', U2, D, D', D2, F, F', F2, B, B', B2

### Implemented until now
- Representation of the cude with lists of lists
- Implemented all possible moves
- Saving the moves given as argument in a list
- Scrambling the cube based on the input
- Printing the cube (lists of lists)
- Started to implement phase1 of the algorithm that solves the cube

### Corrections that need to be done
- When a move is made on a side, I update only the corresponding side BUT a move in a side affects multiple other sides so I need to update the move functions

### Resources
- http://iamthecu.be/ (representing the cube)
- https://ruwix.com/online-rubiks-cube-solver-program/ (moves of cube)
- https://ruwix.com/the-rubiks-cube/notation/ (moves notation of cube)
- https://www.ryanheise.com/cube/human_thistlethwaite_algorithm.html (algorithm)