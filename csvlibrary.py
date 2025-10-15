

def normalize(normalizing_list):
    number_normalizing = 0
    for i in normalizing_list:
        number_normalizing += i
    for i in range(0,len(normalizing_list)):
        normalizing_list[i] /= number_normalizing
    return normalizing_list

def pack(package_previous,number_of_peeps,iterations,pack_list):
    package_previous+=[0]
    package_previous[-1]=[number_of_peeps,iterations]+pack_list
    return package_previous

def report(package,filename):
    bill = ""
    for i in range(0,len(package)):
        bill += (str(package[i])[1:-1]+"\n")
    open(str(filename),"w").write(bill)

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