def largest_product(series, size):
    numbers = list(series)
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    for check in numbers:
        try:
            int(check)
        except:
            raise ValueError("digits input must only contain digits")

    result = 0
    product = 1
    for i in range(len(numbers)):
        if (i + size) <= len(numbers):
            for aux in range(i, i + size):
                product = product * int(numbers[aux])
            if product > result:
                result = product
            product = 1
        else:
            break
    return result

