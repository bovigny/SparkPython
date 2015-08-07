__author__ = 'cbovigny'
import sys
from random import random
from operator import add

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0
    count =0
    for i in range(0,100000) :
        count += f(i)

    print("Pi is roughly %f" % (4.0 * count / 100000))

