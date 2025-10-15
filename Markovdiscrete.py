import random
import time
focus = 0
peeps = int(input("how many people are playing? ")) #User inputs the amount of people
num = int(input("how many rounds? ")) #User inputs the amount of people
countl = [0]*peeps #Create string to count the amount of times the focus was on each person
stime = time.perf_counter() #records the time before the start of the iterations
for x in range(0,num): #repeat for the specified number of rounds
    if focus == 0:
        focus = random.randint(1,peeps-1) #The number 1 person chooses a random person
    else:
        focus = random.randint(0,a-1) #The person chooses a random person with a lower number than them
    countl[focus] += 1 #Adds one at the index on the counting list
for x in range(0,len(countl)):  #Normalizes the count of each index so it represnted as a percent/100
    countl[x-1] /= (.01*num)
print("runtime: "+str(time.perf_counter() - stime)) #prints the time that it took to iterate
print(countl) # prints the output
