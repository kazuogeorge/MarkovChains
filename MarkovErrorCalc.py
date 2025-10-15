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

eroor = 10**(-int(input("what is the error? 10^-")))
iteres = int(input("Slice from 3 to: "))

stime = time.perf_counter()
boll = [0,0,0]

for peepsie in range(3,iteres):
    error = 10
    num = 0
    initial = bb_matrices(peepsie, 1)
    transit = bb_matrices(peepsie, 0)
    while error > eroor:
        error = sum([abs(b-a) for a, b in zip(initial, bb_matrix_mult(initial,transit))])
        print(error)
        initial = bb_matrix_mult(initial,transit)
        num +=1
    boll += [num]

print(time.perf_counter()-stime)
print(boll)
