import itertools

def get_max(l, n):
    return sorted(l)[-n:]

def clamp(n: int, minnum: int, maxnum: int) -> int:
    if n > maxnum:
        n = maxnum
    elif n < minnum:
        n = minnum
    return n

def has_duplicate(colors, error_msg: str, num: int) -> bool:
    for a, b in itertools.combinations(colors, 2):
        if(a == b):
            print(error_msg)
            return True
    return False