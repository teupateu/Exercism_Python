import sys

def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = []
    result = -1
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if i*j > result:
                if isPalindrome(i*j):
                    factors.clear()
                    result = i*j
                    factors.append([i,j])
            elif i*j == result:
                factors.append([i,j])
    if result == -1:
        return None, []
    return result, factors


def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = []
    result = sys.maxsize
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if i*j < result:
                if isPalindrome(i*j):
                    factors.clear()
                    result = i*j
                    factors.append([i,j])
            elif i*j == result:
                factors.append([i,j])
    if result == sys.maxsize:
        return None, []
    return result, factors

def isPalindrome(number):
    string = str(number)
    if string == string[::-1]:
        return True
    return False
