# It all started in parking garage...
before UVA marching band goes out to play for their pre-game show (where we play things like [this](https://www.youtube.com/watch?v=629vBUcy-Fc)), we congregate in the stadiums parking garage, waiting to be told to go in. There, we play a few different games to pass the time. One of them, I am going to call "BB."

The game works like this: there are a bunch of people in a circle, and they are all numbered (those who know this game idependently, know that the first and last person have special names, but that's not important). One person starts with the "focus," and they call out their number, and then the number of somebody else in the circle. That person has to call out their number while staying in time, and then calls out the number of somebody else in the circle. The rest of the people without the "focus" keep a beat by clapping. 

Gif Here

If someone fails to keep the beat, they go the last number slot, and everybody else moves up to fill in their spot. The aim of the game is to hold the number 1 spot for the longest time.

Gif Here

Interesting thing to note here: you can only move up in the game if the person in front of you loses, so the optimal play is to always pass the "focus" to a person with a lower number than you. If people played entirely randomly, then each person would have an equal chance to have the "focus" at any point in time. The math would be easy here, it would be: 100% / number of people. 

Which got me thinking "How would I go about calculating the chance of each person having the focus, provided they play optimally?"

(Small side note here: in optimal play, the person at the number 1 spot can choose whoever they want, because they don't need to move up)

What I thought I needed first was a database of some of the simpler distributions. I had been looking for an excuse to use the basic Python I had been learning in class, so I wrote myself a basic program.
```python
import random
import time
focus = 0
peeps = int(input("how many people are playing? ")) 
num = int(input("how many rounds? "))
countl = [0]*peeps 
stime = time.perf_counter()
for x in range(0,num):
    if focus == 0:
        focus = random.randint(1,peeps-1)
    else:
        focus = random.randint(0,a-1)
    countl[focus] += 1
for x in range(0,len(countl)):
    countl[x-1] /= (.01*num)
print("runtime: "+str(time.perf_counter() - stime))
print(countl) 
```
Using the law of large numbers, the more iterations through this program, the more accurate the output of percent chances. With this first program, I generated some basic, rough estimates of the chance distrubutions like:
```python
how many people are playing? 3
how many rounds? 1000000
runtime: 0.8723384190234356
[44.4515, 33.3222, 22.2263]
```
Able to rip through a million iterations in less than a second seems nice, but later it's easy to look back and see just how slow this program would have been to run to get an accurate database of distributions.
Thankfully I already had an idea of how to improve my approach. Instead of having a single focus, I could split the chance of the focus between the available choices. This would entirely eliminate the need for any randomness in the program. Instead of utilizing the law of large numbers, the distribution improves over iteration because the chance distribution as number of rounds increase approaches the chance distribution at any index and a sufficiently large amount of rounds.
```python
import time
peeps = int(input("how many people are playing? ")) 
num = int(input("how many iterations? "))
chancel = [0] + [1/(peeps-1)]*(peeps-1) 

stime = time.perf_counter()
for i in range(num):
    newl = [0] * peeps  
    for x in range(1,len(chancel)):
        newl[x]=chancel[0]*1/(peeps-1) 
    for x in range(1,len(chancel)):
        for b in range(x): 
            newl[b]+=chancel[x]/x
    chancel = newl 
print("runtime: "+str(time.perf_counter() - stime)) 
print(chancel)
```
With this program, and the same inputs I got:
```python
how many people are playing? 3
how many iterations? 1000000
runtime: 2.2199329070281237
[0.4444444444444445, 0.33333333333333337, 0.22222222222222227]
```
While this has about 3 times the runtime of the first program, it also has 5 times the amount of accurate digits. To fully quantify the difference the new program makes, I graphed both's convergence vs. time for intervals of 50,000 iterations
