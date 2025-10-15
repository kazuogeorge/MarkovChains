import time
peeps = int(input("how many people are playing? "))
e = .01*float(input("how much error is acceptable?(in percent) "))
l = [0] + [1/(peeps-1)]*(peeps-1)
error = 1
num = 0

stime = time.perf_counter()
while error>e:
    error = 0
    ln = [0] * peeps
    for x in range(1,len(l)):
        ln[x]=l[0]*1/(peeps-1)
    for x in range(1,len(l)):
        for b in range(x):
            ln[b]+=l[x]/x
    for x in range(len(l)):
        if not l[x]==0:
            error+= abs(ln[x]/l[x]-1)
        else:
            error+=1
    num += 1
    l = ln
print(time.perf_counter()-stime)
print(num)
print(l)

#General function for number of trials to reach .0000000001 error: f(x) = 1.25x + 28