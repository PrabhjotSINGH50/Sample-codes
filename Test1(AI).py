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



def dont_give_me_five(start, end):
    # Count integers in [start, end] whose (base-10) digits do NOT contain '5'.
    def count_upto(n: int) -> int:
        # Count integers x in [0, n] with no digit '5'
        if n < 0:
            return 0
        s = str(n)
        L = len(s)
        # powers of 9: each digit has 9 choices (0-9 except '5')
        pow9 = [1] * (L + 1)
        for i in range(1, L + 1):
            pow9[i] = pow9[i - 1] * 9

        total = 0
        for i, ch in enumerate(s):
            d = int(ch)
            left = L - i - 1
            if d < 5:
                total += d * pow9[left]
            elif d == 5:
                total += 5 * pow9[left]
                return total  # any continuation would contain a '5'
            else:  # d > 5
                total += (d - 1) * pow9[left]
        # n itself has no '5'
        return total + 1

    if start >= 0:
        return count_upto(end) - count_upto(start - 1)
    elif end < 0:
        # Map negatives [-X, -Y] to positives [Y, X]
        return count_upto(-start) - count_upto(-end - 1)
    else:
        # start <= 0 <= end : negatives + zero + positives
        return count_upto(-start) + count_upto(end) - 1


# # quick checks
# print(dont_give_me_five(1, 9))     # 8
# print(dont_give_me_five(4, 17))    # 12
# print(dont_give_me_five(-5, 5))    # 9
# print(dont_give_me_five(-20, -1))  # 18
# print(dont_give_me_five(-20, 20))  # 37




