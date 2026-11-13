# Author: Brian A. Miller
# E-mail address: bam5@comcast.net
# GitHub repositories: https://github.com/brian-a-miller
# Date (v1): Friday, November 13, 2026

import math

# The body of the following method copied from Google AI Overview answer
# to question "rules for determining programmatically if a number is prime"
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    limit = math.isqrt(num)
    for i in range(5, limit + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True