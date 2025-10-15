import time
peeps = int(input("how many people are playing? "))
num = int(input("how many iterations? "))
chancel = [0] + [1/(peeps-1)]*(peeps-1)

stime = time.perf_counter()
for i in range(num):
    newl = [0] * peeps
    for x in range(1,len(l)):
        newl[x]=l[0]*1/(peeps-1)
    for x in range(1,len(l)):
        for b in range(x):
            newl[b]+=l[x]/x
    chancel = newl
print(time.perf_counter() - stime)
print(l)
