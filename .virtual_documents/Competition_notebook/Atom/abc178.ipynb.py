x1 = 1


y1 = 0


#export
def helper(x):
    """prints help"""
    print(x)
    return x


#get_ipython().getoutput("/usr/bin/env python3")
import sys


def solve(x: int):
    helper(x)
    return (1 - x)


assert solve(x1) == y1



