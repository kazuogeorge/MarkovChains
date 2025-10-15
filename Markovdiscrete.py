import random
focus = 0
peeps = int(input("how many people are playing? "))
num = int(input("how many rounds? "))
l = [0]*peeps
for x in range(0,num):
    if focus == 0:
        focus = random.randint(1,peeps-1)
    else:
        focus = random.randint(0,a-1)
    l[focus] += 1
print(l)
for x in range(0,len(l)):
    l[x-1] /= (.01*num)
print(l)
