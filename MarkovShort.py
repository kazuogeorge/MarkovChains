import time
peeps = int(input("how many people are playing? ")) #User inputs the number of people
num = int(input("how many iterations? ")) #User inputs the number of iterations
chancel = [0] + [1/(peeps-1)]*(peeps-1) #Creates a list with the chance of each position after the first round

stime = time.perf_counter() #records the time before the start of the iterations
for i in range(num):
    newl = [0] * peeps  # Creates a transition list with the right number of indexes for the people
    for x in range(1,len(chancel)):
        newl[x]=chancel[0]*1/(peeps-1) #The number 1 person gives their chance evenly across the rest of the people
    for x in range(1,len(chancel)):
        for b in range(x): #Each other person gives their chance evenly across the rest of the people with numbers lower than them
            newl[b]+=chancel[x]/x
    chancel = newl #writes the transition list to the main list
print("runtime: "+str(time.perf_counter() - stime)) #prints the time that it took to iterate
print(chancel)
