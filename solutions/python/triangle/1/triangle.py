def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    elif a == b and b == c:
        return True
    return False
        


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    elif a == b or b == c or a == c:
        return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    elif a != b and b != c and c != a:
        return True
    return False
