# It all started in parking garage...
before UVA marching band goes out to play for their pre-game show (where we play things like [this](https://www.youtube.com/watch?v=629vBUcy-Fc)), we congregate in the stadiums parking garage, waiting to be told to go in. There, we play a few different games to pass the time. One of them, I am going to call "BB."

The game works like this: there are a bunch of people in a circle, and they are all numbered (those who know this game idependently, know that the first and last person have special names, but that's not important). One person starts with the "focus," and they call out their number, and then the number of somebody else in the circle. That person has to call out their number while staying in time, and then calls out the number of somebody else in the circle. The rest of the people without the "focus" keep a beat by clapping. 

Gif Here

If someone fails to keep the beat, they go the last number slot, and everybody else moves up to fill in their spot. The aim of the game is to hold the number 1 spot for the longest time.

Gif Here

Interesting thing to note here: you can only move up in the game if the person in front of you loses, so the optimal play is to always pass the "focus" to a person with a lower number than you. If people played entirely randomly, then each person would have an equal chance to have the "focus" at any point in time. The math would be easy here, it would be: 100% / number of people. 

Which got me thinking "How would I go about calculating the chance of each person having the focus, provided they play optimally?"
(Small side note here: in optimal play, the person at the number 1 spot can choose whoever they want, because they don't need to move up)
I had been looking for an excuse to use the basic Python I had been learning in class, so I wrote myself a basic program.
```python
import random
focus = 0
peeps = int(input("how many people are playing? ")) 
num = int(input("how many rounds? ")) 
countl = [0]*peeps 
for x in range(0,num):
    if focus == 0:
        focus = random.randint(1,peeps-1)
    else:
        focus = random.randint(0,a-1) 
    countl[focus] += 1 
for x in range(0,len(countl)): 
    countl[x-1] /= (.01*num)
print(countl) 
```
Using the law of large numbers, the more iterations through this program, the more accurate the output of percent chances. With this first program, I generated some basic, rough estimates of the chance distrubutions like:
```python

```
