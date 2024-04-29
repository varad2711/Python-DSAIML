def ChkPrime(num):

    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
