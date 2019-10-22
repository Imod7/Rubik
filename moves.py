import colors as col

# move left clockwise
def move_l(l):
    print(col.YELLOW + "Move L" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move left clockwise double
def move_l_double(l):
    print(col.YELLOW + "Move L2" + col.RESET)
    l = l[3:] + l[0:3]
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move left counterclockwise
def move_l_prime(l):
    print(col.YELLOW + "Move L Prime" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move right clockwise
def move_r(l):
    print(col.YELLOW + "Move R" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move right clockwise double
def move_r_double(l):
    print(col.YELLOW + "Move R2" + col.RESET)
    l = l[3:] + l[0:3]
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move right counterclockwise
def move_r_prime(l):
    print(col.YELLOW + "Move R Prime" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move up clockwise
def move_u(l):
    print(col.YELLOW + "Move U" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move up clockwise double
def move_u_double(l):
    print(col.YELLOW + "Move U2" + col.RESET)
    l = l[1:] + l[:1]
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move up counterclockwise
def move_u_prime(l):
    print(col.YELLOW + "Move U Prime" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move down clockwise
def move_d(l):
    print(col.YELLOW + "Move D" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move down clockwise double
def move_d_double(l):
    print(col.YELLOW + "Move D2" + col.RESET)
    l = l[3:] + l[0:3]
    l = l[3:] + l[0:3]
    print(l)
    return (l)

# move down counterclockwise
def move_d_prime(l):
    print(col.YELLOW + "Move D Prime" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move front clockwise
def move_f(l):
    print(col.YELLOW + "Move F" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return(l)

# move front clockwise double
def move_f_double(l):
    print(col.YELLOW + "Move F2" + col.RESET)
    l = l[1:] + l[:1]
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move front counterclockwise
def move_f_prime(l):
    print(col.YELLOW + "Move F Prime" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move back clockwise
def move_b(l):
    print(col.YELLOW + "Move B" + col.RESET)
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move back clockwise double
def move_b_double(l):
    print(col.YELLOW + "Move B2" + col.RESET)
    l = l[1:] + l[:1]
    l = l[1:] + l[:1]
    print(l)
    return (l)

# move back counterclockwise
def move_b_prime(l):
    print(col.YELLOW + "Move B Prime" + col.RESET)
    l = l[3:] + l[0:3]
    print(l)
    return (l)
