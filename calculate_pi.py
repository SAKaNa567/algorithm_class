
import random
import math
def pi(n):
    ansl = []
    for num in range(10):
        inCircle= 0
        for count in range(0, n):
            x = random.random()
            y = random.random()
            d = (x - 0.5)**2 + (y - 0.5)**2
            if d < 0.25: inCircle += 1
        count += 1
        ans = 4.0 * inCircle / n
        ansl.append(ans)
    return ansl

print pi(1)
print pi(10)

print pi(100)
print pi(1000)
print pi(10000)
print pi(100000)
