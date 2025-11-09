# Your mission, should you accept it, is to return the count of 
# all integers in a given range which do not contain the digit 5
#  (in base 10 representation).
# You are given the start and the end of the integer range.
# The start and the end are both inclusive.

# Examples:

# 1,9 -> 1,2,3,4,6,7,8,9 -> return 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12

# The result may contain fives. ;-)
# The start will always be smaller than the end. Both numbers can be also negative.

# The regions can be very large and there will be a large number of test cases.
# So brute force solutions will certainly time out!

# Good luck, warrior!





import math


def _count(v: int) -> int:
    res = 0
    for mag in range(int(math.log10(v)), -1, -1):
        digit, v = divmod(v, 10**mag)
        res += digit * 9**mag
        if digit == 5:
            return res - 1
        elif digit > 5:
            res -= 9**mag
    return res


def dont_give_me_five(start: int, end: int) -> int:
    if end < 0:
        start, end = abs(end), abs(start)
    fives = _count(end) if end else 0
    match start:
        case 0:
            return fives + 1
        case 1:
            return fives
        case start if start < 0:
            return fives + _count(abs(start)) + 1
        case _:
            return fives - _count(start - 1)