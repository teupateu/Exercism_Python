import math

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    decimal = 0
    power = len(digits)
    if power == 0:
        return [0]
    result = []
    for i in digits:
        if i < 0 or i >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal = decimal + i * pow(input_base, power - 1)
        power = power - 1
    if decimal == 0:
        return [0]
    while decimal != 0:
        result.append(decimal % output_base)
        decimal = decimal // output_base
    result.reverse()
    return result