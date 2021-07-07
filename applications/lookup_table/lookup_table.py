# Your code here
import math
import random
# import timeit
import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

slowfun_cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # check cache for values
    if (x, y) not in slowfun_cache:
        slowfun_cache[(x, y)] = slowfun_too_slow(x, y) # if not add value to cache
    return slowfun_cache[(x, y)]



# Do not modify below this line!
start_time = time.time()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time = time.time()

print(f'It takes {end_time - start_time} to count to 50,000.')
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))