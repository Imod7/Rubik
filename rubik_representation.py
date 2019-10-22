# represent the cube with numbers

# initial state of left
left_side = [[1, 4, 7],
             [7, 15, 24],
             [24, 21, 18],
             [18, 10, 1]]

# initial state of right
right_side = [[3, 6, 9],
              [9, 17, 26],
              [26, 23, 20],
              [20, 12, 3]]

# initial state of up
upper_side = [[1, 2, 3], 
              [3, 12, 20],
              [20, 19, 18],
              [18, 10, 1]]

# initial state of bottom
down_side = [[7, 8, 9], 
             [9, 17, 26],
             [26, 25, 24],
             [24, 15, 7]]

# initial state of front
front_side = [[1, 2, 3],
              [3, 6, 9],
              [9, 8, 7],
              [7, 4, 1]]

# initial state of back
back_side = [[18, 19, 20],
             [20, 23, 26],
             [26, 25, 24],
             [24, 21, 18]]


####################################
# IDEAS on the Cube's representation
####################################

# represent the layers of the cube ???
bottom = {'f_l_corner' : 'wog', 
          'f_r_corner' : 'obw', 
          'b_l_corner' : 'rgw', 
          'b_r_corner' : 'brw',
          'f_edge': 'ow',
          'l_edge': 'wg',
          'r_edge': 'bw',
          'b_edge': 'rw',
          'center': 'w'}

middle = {'f_l_edge': 'og', 
          'f_r_edge': 'ob', 
          'b_l_edge': 'rg', 
          'b_r_edge': 'br',
          'f_center': 'o',
          'l_center': 'g',
          'r_center': 'b',
          'b_center': 'r'}

top    = {'f_l_corner': 'oyg', 
          'f_r_corner': 'oyb', 
          'b_l_corner': 'gyr', 
          'b_r_corner': 'ybr',
          'f_edge': 'yo',
          'l_edge': 'yg',
          'r_edge': 'yb',
          'b_edge': 'yr',
          'center': 'r'}

# represent the pieces of the cube ???
edges_l = ['og', 'yg', 'rg', 'wg']
corners_l = ['oyg', 'yrg', 'ogw', 'rgw']
center_l = ['g']
edges_r = ['ob', 'yb', 'rb', 'bw']
corners_r = ['oyb', 'obw', 'ybr', 'brw']
center_r = ['b']