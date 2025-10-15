import time
interlist = [0, 0, 0, 40, 28, 28, 29, 29, 30, 31, 32, 33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 43, 44, 44, 45, 45, 45, 46, 46, 46, 47, 47, 47, 48, 48, 48, 48, 49, 49, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60]

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

def report(package,filename):
    bill = ""
    for i in range(0,len(package)):
        bill += (str(package[i])[1:-1]+"\n")
    open(str(filename),"w").write(bill)

def pack(package_previous,number_of_peeps,iterations,pack_list):
    package_previous+= [0]
    package_previous[-1] = [number_of_peeps,iterations]+pack_list
    return package_previous

print("slicing from 0-100")
stime = time.perf_counter()
finalbill = []

for peepsie in range(3,len(interlist)):
    initial = bb_matrices(peepsie,1)
    transit = bb_matrices(peepsie,0)
    for x in range(interlist[peepsie]):
        initial = bb_matrix_mult(initial,transit)
    finalbill = pack(finalbill,peepsie,interlist[peepsie],initial)

report(finalbill,"datasheet.csv")
print("runtime: "+str(time.perf_counter()-stime))