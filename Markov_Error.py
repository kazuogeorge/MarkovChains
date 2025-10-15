import random
import time
peeps = int(input("how many people are playing? "))
e = .01*float(input("how much error is acceptable?(in percent) "))
num = 0
a = 0
l = [0]*peeps
error = 1

stime = time.perf_counter()
while error > e:
    if a == 0:
        a = random.randint(1,peeps-1)
    else:
        a = random.randint(0,a-1)
    num += 1
    if not l[a]==0:
        error = 1/l[a]
    l[a] += 1
print(time.perf_counter()-stime)
print(num)
print(l)

#General function for number of trials to reach .001 error: f(x) = 14716.5476x + 180576.738

