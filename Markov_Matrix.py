import time
def bb_matrices(peeps,typ):
    if typ:
        initial_bb_matrix = [1]+[0]*(peeps-1)
        return initial_bb_matrix
    else:
        transition_bb_matrix = [[0]+[1/(peeps-1)]*(peeps-1)]
        for x in range(1,peeps):
            transition_bb_matrix+=[0]
            transition_bb_matrix[-1] = [1/x]*x+[0]*(peeps-x)
        return transition_bb_matrix

def bb_matrix_mult(i,t):
    multed_matrix = [0]*len(i)
    for b in range(len(i)):
        summ = 0
        for a in range(len(t)):
            summ += i[a]*t[a][b]
        multed_matrix[b] = summ
    return multed_matrix

peepsie = int(input("how many people are playing? "))
iterations = int(input("how many iterations? "))

stime = time.perf_counter()

initial = bb_matrices(peepsie,1)
transit = bb_matrices(peepsie,0)

i = initial
for x in range(iterations):
    i = bb_matrix_mult(i,transit)
print(time.perf_counter()-stime)
print(i)

