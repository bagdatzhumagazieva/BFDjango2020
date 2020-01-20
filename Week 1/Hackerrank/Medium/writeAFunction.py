def is_leap(n):
    leap = False
    a = int(n % 4)
    b = int(n % 100)
    c = int(n % 400)
    if ((a == 0 and b != 0) or (c == 0)):
        leap = True
    else:
        leap = False
    return leap