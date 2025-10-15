import time
ratilst= [0.40909091,0.27272727,0.18181818,0.13636364]
error = 10**-7
outlst = []
for i in range(len(ratilst)):
    x = 0
    while x < 1/error:
        x+=1
        if ratilst[i] == 0:
            outlst += ["0"]
            break
        elif abs(x*ratilst[i]-round(ratilst[i]*x))<error:
            outlst+=[str(int(round(ratilst[i]*x)))+"/"+str(x)]
            print(str(int(round(ratilst[i]*x)))+"/"+str(x))
            break

print(outlst)