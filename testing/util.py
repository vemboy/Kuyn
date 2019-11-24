import math
from math import floor

def get_max(l, n):
    return sorted(l)[-n:]

def clamp(n: int, minnum: int, maxnum: int) -> int:
    if n > maxnum:
        n = maxnum
    elif n < minnum:
        n = minnum
    return n
