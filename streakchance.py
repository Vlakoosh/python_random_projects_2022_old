import random

streak_number = 0
streak = 0
flips = []


for experiment in range(10000):

    for i in range(100):
        flips.append(random.randint(0,1))
    
    for i in range(len(flips)):
        if flips[i] == flips[i-1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            streak_number += 1
    flips = []
print('Chance of streak: %s%%' % (streak_number / 10000))