# move left clockwise
def move_l(l):
    return (l[3:] + l[0:3])

# move left counterclockwise
def move_l_prime(l):
    return (l[1:] + l[:1])

# move left clockwise
def move_r(l):
    return (l[3:] + l[0:3])

# move left counterclockwise
def move_r_prime(l):
    return (l[1:] + l[:1])

# move up clockwise
def move_u(l):
    return (l[1:] + l[:1])

# move up counterclockwise
def move_u_prime(l):
    return (l[3:] + l[0:3])

# move down clockwise
def move_d(l):
    return (l[3:] + l[0:3])

# move down counterclockwise
def move_d_prime(l):
    return (l[1:] + l[:1])

# move front clockwise
def move_f(l):
	# print("Move F")
    return (l[3:] + l[0:3])

# move front counterclockwise
def move_f_prime(l):
    return (l[1:] + l[:1])

# move back clockwise
def move_b(l):
    return (l[1:] + l[:1])

# move back counterclockwise
def move_b_prime(l):
    return (l[3:] + l[0:3])
