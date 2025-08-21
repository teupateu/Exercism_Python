def is_armstrong_number(number):
    copy = number
    result = 0
    while number != 0:
        result += (number % 10) ** number_of_digits(copy)
        number = number // 10
    return copy == result

def number_of_digits(number):
    cnt = 0
    while number != 0:
        number = number // 10
        cnt += 1
    return cnt

print(is_armstrong_number(153))