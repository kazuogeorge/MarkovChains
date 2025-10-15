import numpy as np
numopeople = int(input("How many people are playing? "))

def bb_broken_matrices(peeps,typ):
    if typ:
        initial_bb_matrix = [1]+[0]*(peeps-1)
        return initial_bb_matrix
    else:
        transition_bb_matrix = [[-1]+[1/(peeps-1)]*(peeps-1)]
        for x in range(1,peeps):
            transition_bb_matrix+=[0]
            transition_bb_matrix[-1] = [1/x]*x+[-1]+[0]*(peeps-x-1)
        return transition_bb_matrix


mat = bb_broken_matrices(numopeople,0)
mat = np.array(mat).T
mat[0] = [1]*numopeople
mat = np.linalg.inv(mat)

sat = [[1]+[0]*(numopeople-1)]
sat = np.array(sat).T

print((mat@sat).T)


